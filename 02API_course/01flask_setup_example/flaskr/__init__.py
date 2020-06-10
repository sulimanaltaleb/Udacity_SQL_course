from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    @app.route('/simley')
    def simley():
        return jsonify({'message':'Hello, World!'})
    @app.route('/messages')
    def read():
        return jsonify({'messages': [1,2,3,4,5,6]})

    

    return app