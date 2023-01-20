from shared import env
from flask import Flask
from waitress import serve
from routes.upload import upload
from routes.load import load
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app)

@app.get("/")
def index():
    return {
        'name': env('APP_NAME'),
        'version': env('APP_VERSION')
    }

app.register_blueprint(upload)
app.register_blueprint(load)


if __name__ == '__main__':
    port = int(env('SERVER_PORT', 5000))
    print(f'Inicializando o B3 na porta {port}')
    serve(app, listen=f'*:{port}')
