This is a blogging app based on the [Flask tutorial](https://github.com/pallets/flask/tree/1.0.2/examples/tutorial).

`run.ps1` is a Powershell script that runs the website in development mode. Development mode has an interactive debugger and restarts the server upon code change.

# Layout

* `flaskr/` - a Python package; contains application code
    * `__init__.py` - contains the application factory and tells Python to treat `flaskr` as a package
    * `db.py` - handles requests to DB
    * `schema.sql` - schema for `user` and `post` tables
* `tests/` - contains tests
* `env/` - the Python virtual environment (not uploaded to Github)
* `templates/` - 
* `static/` - 
* `auth.py` - 
* `blog.py` - 
* `setup.py` - 
* `MANIFEST.in` - 
