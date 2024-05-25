# User Authentication Service

- Welcome to my User Authentication Service! This project is built using Flask and provides API routes for user registration, login, and profile management. Below are the key learning objectives I aimed to cover in this project:

1. How to declare API routes in a Flask app
API routes are endpoints that handle specific HTTP requests. In Flask, routes are declared using the @app.route decorator. Here is an example of how I declared a simple route:

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)

In this example, I declared the /hello endpoint, which responds to GET requests with a JSON message.


2. How to get and set cookies
Cookies are used to store data on the client side and send it with every request to the server. In Flask, I can get and set cookies using the request and response objects. Here’s an example:

from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    response = make_response("Cookie is set")
    response.set_cookie('username', 'JohnDoe')
    return response

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(debug=True)

In this example, the /set_cookie route sets a cookie named username, and the /get_cookie route retrieves the value of that cookie.

3. How to retrieve request form data
Form data is data sent by a client as part of an HTTP POST request. In Flask, I can retrieve form data using the request.form object. Here’s an example:

from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f'Username: {username}, Password: {password}'

if __name__ == '__main__':
    app.run(debug=True)

In this example, the /login route retrieves username and password from the form data submitted via a POST request.

4. How to return various HTTP status codes
HTTP status codes indicate the result of an HTTP request. In Flask, I can return different status codes using the make_response function or by specifying the status code in the return statement. Here’s an example:

from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/success')
def success():
    return jsonify(message="Success!"), 200

@app.route('/not_found')
def not_found():
    return make_response(jsonify(message="Resource not found"), 404)

@app.route('/error')
def error():
    return jsonify(message="Internal server error"), 500

if __name__ == '__main__':
    app.run(debug=True)

In this example, different routes return different HTTP status codes: 200 for success, 404 for not found, and 500 for an internal server error.

Getting Started
To run the application, ensure you have Python and Flask installed. You can install Flask using pip:

pip install Flask


Run the application:

python app.py
