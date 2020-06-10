from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data = [{
        'description' = 'Todo 1'
    },{
        'description' = 'Todo 2'
    },{
        'description' = 'Todo 3'
    }])


    #To run this application you have to type in terminal
    # FLASK_APP=app.py FLASK_DEBUG=True flask run