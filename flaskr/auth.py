from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import functools
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# create a Blueprint named 'auth'
    # a Blueprint is a collection of Views (pages), templates, and static pages
    # Blueprints are useful for organizing an app into distinct components
bp = Blueprint('auth', __name__, url_prefix='/auth')
# now we will create 3 Views for this Blueprint - /register, /login, and /logout
    # Views = functions w/ the `bp.route(URL, methods)` decorator

# View 1 - /auth/register
@bp.route('/register', methods=('GET', 'POST'))
def register():
    """ parse HTTP POST request 
    validate username+password;  if success, put in DB;  else, flash error msg
    either way, render the `auth/register.html` template
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))  
            # url_for() converts a View name (`auth.login`) to its corresponding URL
        else:
            flash(error)
            # flash() displays a message 
            # when get_flashed_messages() is called in base.html

    return render_template('auth/register.html')

# View 2 - /auth/login
@bp.route('/login', methods=('GET', 'POST'))
def login():
    """ parse HTTP POST request 
    validate username+password; if success, store username in session;
                                else, flash error msg
    either way, render the `auth/login.html` template
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        # session = dict that persists data across requests
            # if login succeeds, we add the username to the session
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        else:
            flash(error)

    return render_template('auth/login.html')

# @bp.before_app_request - func executes when any of bp's URLs are accessed
@bp.before_app_request
def load_logged_in_user():
    """ check if session has a user_id;     if so, load it """
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

# View 3 - /auth/logout
@bp.route('/logout')
def logout():
    """ logging out is as simple as clearing the session """
    session.clear()
    return redirect(url_for('index'))

# login_required is a decorater that makes log-in mandatory to access a View
def login_required(view):
    """ if user is not logged-in, redirect to /auth/login
        auth is the Blueprint   login is the View   auth.login is the Endpoint
    """
    @functools.wraps(view)  # turns the parent function into a decorator
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view