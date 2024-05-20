# Basic Authentication

## General
### What authentication means
Authentication is the process of verifying the identity of a user or a system. In the context of web applications, it ensures that users or systems accessing the application are who they claim to be. This is typically achieved through credentials such as usernames and passwords, tokens, or other verification methods.

### What Basic authentication means
Basic authentication is a simple authentication scheme built into the HTTP protocol. In Basic authentication, the client sends the username and password encoded in Base64 as part of the HTTP request's Authorization header. The server decodes this information and validates the credentials. If valid, the server grants access; otherwise, it denies access.

### How to send the Authorization header
To send the Authorization header in an HTTP request using Python, you can use the requests library.
