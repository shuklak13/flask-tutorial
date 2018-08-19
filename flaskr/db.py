import sqlite3
import click
from flask.cli import with_appcontext

from flask import current_app, g
# g = namespace; holds data during a connection request
# current_app = pointer to the Flask application handling a request

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES    # SQL-to-Python type parser
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# create a CLI command `flask init-db` that calls init_db()
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    """ close_db() upon termination, and add the `flask init-db` command """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)