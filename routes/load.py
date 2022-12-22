from flask import Blueprint, request, render_template

load = Blueprint("load", __name__)

@load.route("/load", methods = [ "GET", "POST"])
def load_file():
    return render_template("load.html")
