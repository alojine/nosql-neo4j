from db import NetworkDB
from dotenv import load_dotenv
from flask import Flask, g
import os
from blueprints.network import networks_blueprint
from blueprints.user import users_blueprint
load_dotenv()

def create_app():

    app = Flask(__name__)

    # environment
    URI = os.getenv('NEO4J_URI')
    USER = os.getenv('NEO4J_USER')
    PASSWORD = os.getenv('NEO4J_PASSWORD')

    # database
    @app.before_request
    def before_request():
        g.db = NetworkDB(URI, USER, PASSWORD)

    # blueprints
    app.register_blueprint(networks_blueprint, url_prefix='/networks')
    app.register_blueprint(users_blueprint, url_prefix='/users')

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(host='0.0.0.0', port=8080, debug=True)

