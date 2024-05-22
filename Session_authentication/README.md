# Session Authentication Project

## Learning Objectives

- What Authentication Means
Authentication is the process of verifying the identity of a user or system. In the context of web applications, it typically involves checking credentials like usernames and passwords to ensure that the user is who they claim to be. Successful authentication allows users to access protected resources and services.

- What Session Authentication Means
Session authentication is a method where the server creates a session for a user upon successful login. This session is stored on the server and a session ID is sent to the client as a cookie. On subsequent requests, the server uses this session ID to verify the user's identity, allowing them to remain logged in across multiple requests without re-entering credentials.

- What Cookies Are
Cookies are small pieces of data sent from a server and stored on a user's browser. They are used to remember information about the user, such as session IDs, preferences, and tracking information. Cookies are essential for maintaining state in web applications, which are inherently stateless.

- How to Send Cookies
To send cookies, the server includes a Set-Cookie header in the HTTP response. This header contains the cookie name, value, and optional attributes such as expiration time, domain, path, and security flags. The browser then stores this cookie and sends it with subsequent requests to the same server.


### Example:

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Setting a cookie")
    resp.set_cookie('sessionID', '123456')
    return resp

- How to Parse Cookies
Parsing cookies involves reading the Cookie header from incoming HTTP requests. This header contains all cookies previously set by the server. The server then extracts the relevant cookie values to identify and authenticate the user.

### Example:

from flask import Flask, request

app = Flask(__name__)

@app.route('/get_cookie')
def get_cookie():
    session_id = request.cookies.get('sessionID')
    return f'The session ID is {session_id}'

