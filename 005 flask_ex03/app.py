from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://amy@localhost:5432/todoapp_development'

db=SQLAlchemy(app)

class Todo(db.Model):
    __tablename__='todos'
    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<todo {self.id} {self.description}>'
db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data = Todo.query.all())

    #To run this application you have to type in terminal
    # FLASK_APP=app.py FLASK_DEBUG=True flask run
    # insert into todos(description) values ('Maisa');