.\env\Scripts\activate
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask init-db   # custom command;   see db.py for details
flask run