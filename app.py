from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World"

@app.route('/about')
def about():
    return "About Us Page"

@app.route('/htmlDemo')
def htmlDemo():
    return "<h1> Welcome to my site </h1><p> this is a paragraph </p> "

@app.route('/api')
def api():
    return jsonify({"message" : "Hello" , "status" : "success"})

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'

@app.route('/search')
def search():
    term = request.args.get('term')
    return f"you searched for: {term}"

if __name__ == '__main__':
    app.run()
