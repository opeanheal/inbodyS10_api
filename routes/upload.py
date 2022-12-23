from flask import Blueprint, request, make_response, send_file
from controllers.ReportController import report as make_report

upload = Blueprint('upload', __name__)

@upload.route("/upload", methods = ["GET", "POST"])
def upload_file():
    if 'csv-file' not in request.files:
        return make_response(
            {'success': False},
            404
        )
    file = request.files['csv-file']
    if file.filename == '':
        return make_response(
            {'success': False, 'error': 'File not found'},
            404
        )
    print(f'request{request.form.get("indexes")}')

    pdf = make_report(
        filename = file,
        name = request.form.get("name").upper(),
        indexes = request.form.get("indexes"))

    return send_file(pdf,"report.pdf", as_attachment=True, download_name="report.pdf")
