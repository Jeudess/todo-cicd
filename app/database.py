import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_database(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
