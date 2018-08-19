import os
from flask import Flask

def create_app(test_config=None):
    """ application factory function
    returns a Flask application (instance of Flask class)
    """

    # create and configure the app
        # instance_relative_config = True
            # creates the instance folder in the parent of the flaskr directory
        # instance folder contains config files
            # config files = secrets, database, etc. - stuff not on git
    app = Flask(__name__, instance_relative_config=True)

    # set configuration for app
        # SECRET_KEY is a secure value (ex: os.urandom(16)); do NOT share on git
        # DATABASE is the path to the DB
    app.config.from_mapping(
        SECRET_KEY='dev',   # placeholder
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists (mkdir if it doesn't)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # add DB functionality to the app
    from . import db
    db.init_app(app)

    # add auth functionality to the app
    from . import auth
    app.register_blueprint(auth.bp)

    return app

create_app()