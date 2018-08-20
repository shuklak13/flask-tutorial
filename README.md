This is a blogging app based on the [Flask tutorial](https://github.com/pallets/flask/tree/1.0.2/examples/tutorial).

`run.ps1` is a Powershell script that runs the website in development mode. Development mode has an interactive debugger and restarts the server upon code change.


# URLs

* http://127.0.0.1:5000/hello
* http://127.0.0.1:5000/auth/register
* http://127.0.0.1:5000/auth/login
* http://127.0.0.1:5000/auth/logout


# Layout

* `flaskr/` - a Python package; contains application code
    * `__init__.py` - contains the application factory and tells Python to treat `flaskr` as a package
    * `db.py` - handles requests to DB
    * `schema.sql` - schema for `user` and `post` tables
    * `auth.py` - a blueprint consisting of the `auth/register`, `auth/login`, and `auth/logout` views
    * `blog.py` - a blueprint consisting of the `/`, `/create`, `/<int:id>/update`, and `/<int:id>/delete` views
    * `templates/` - contains Jinja files (HTML files that evaluate Python)
        * `base.html` - the base template
            * has a link to login/logout
            * displays `flash()` messages
            * contains empty `{% block %}`s (title, header, and content) which are filled in by inheriting templates
                * note that the title/header `block`s can be nested if you want them to be shared (see any of the `auth/` files for an example)
        * `auth/`
            * `register.html`
            * `login.html`
        * `blog/`
            * `index.html`
    * `static/` - CSS, Javascript, images, etc. (can be accessed in Flask via `url_for('static', filename='...')`)
* `tests/` - contains tests
* `env/` - the Python virtual environment (not uploaded to Github)
* `templates/` - 
* `static/` - 
* `setup.py` - 
* `MANIFEST.in` - 
