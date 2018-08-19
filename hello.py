from flask import Flask

# Flask is a class
# Flask applications are instances of the Flask class
app = Flask(__name__)
# here, we make our Flask app a global variable
# but best practice is to make our Flask instance inside of a function,
    # called the 'application factory'

@app.route('/')
def hello():
    return 'Hello, World!'