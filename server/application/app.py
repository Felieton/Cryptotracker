from flask import Flask
from safrs import SAFRSBase, jsonapi_rpc, SAFRSAPI
from application.db import db, migrate
from application.models.user import User
from application.models.crypto_currency import CryptoCurrency
from flask_cors import CORS


def create_api(app, HOST="localhost", PORT=5000, API_PREFIX=""):
    api = SAFRSAPI(app, host=HOST, port=PORT, prefix=API_PREFIX)
    api.expose_object(User)
    api.expose_object(CryptoCurrency)
    print("Starting API: http://{}:{}/{}".format(HOST, PORT, API_PREFIX))


def create_app(config_filename=None, host="localhost"):
    app = Flask(__name__)
    CORS(app)
    app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///crypto_db.db')
    app.config.update(SQLALCHEMY_TRACK_MODIFICATIONS=False)
    db.init_app(app)
    migrate.init_app(app, db)
    SAFRSBase.db_commit = False
    with app.app_context():
        db.create_all()
        create_api(app, host)
    return app


host_name = 'localhost'
server_app = create_app(host=host_name)


def run_server_app():
    server_app.run(host=host_name)


if __name__ == "__main__":
    run_server_app()
