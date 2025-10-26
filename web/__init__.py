import os

from flask import Flask, render_template, request, jsonify
import requests


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )



    # a simple page that says hello
    @app.route('/')
    def hello():
        try:
            response = requests.get("http://127.0.0.1:8080/greet", params=request.args, timeout=5)
            response.raise_for_status()
            data = response.text

            return render_template("index.html", backend_string = data)
        except requests.RequestException as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500

    return app
