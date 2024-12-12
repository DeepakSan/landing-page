from flask import Flask, render_template
from .helpers.constants import CONFIG_PATH
from .extensions import db, migrate
from . import model

def create_app():
    app = Flask(__name__)
    app.config.from_object(CONFIG_PATH)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def home():
        """
        The homepage of the website, which just renders the index.html template.
        """
        count = db.session.query(model.Count).first()
        count.count += 1
        db.session.commit()
        return render_template('index.html', live_count=count.count)


    return app