from flask import Flask, render_template
from .helpers.constants import CONFIG_PATH
from .helpers.logging import create_logger
from .extensions import db, migrate
from . import model

def create_app(ENV='dev'):
    app = Flask(__name__)

    app.config.from_object(CONFIG_PATH+f'{ENV}Config')
    logger = create_logger(app)
    logger.debug(f"Loading configuration: {CONFIG_PATH + f'{ENV}Config'}")

    db.init_app(app)
    logger.debug(f"Initialized database")
    migrate.init_app(app, db)
    logger.debug(f"migrated/upgraded database")

    @app.route('/')
    def home():
        """
        The homepage of the website, which just renders the index.html template.
        """
        count = db.session.query(model.Count).first()
        count.count += 1
        db.session.commit()
        logger.info(f"{count.count} th visitor visited the website")
        return render_template('index.html', live_count=count.count)


    return app