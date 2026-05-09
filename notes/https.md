# HTTP Basics

## What HTTP is
HTTP stands for HyperText Transfer Protocol.

It is the communication system used by browsers and servers to exchange data on the web.

When I open a website, my browser sends an HTTP request to a server, and the server sends back an HTTP response.

HTTP is the foundation of web traffic.

---

## Client and Server
A client is usually the browser or app making the request.

A server is the machine or service receiving the request and sending back a response.

Example:
- Browser = client
- Website backend = server

---

## Request
A request is what the client sends to the server.

A request usually contains:
- a method
- a path or URL
- headers
- sometimes a body

The request tells the server what the client wants.

Example idea:
A browser asks a server for a page, image, API result, or sends login form data.

---

## Response
A response is what the server sends back to the client.

A response usually contains:
- a status code
- headers
- sometimes a body

The response tells the client whether the request succeeded and includes the returned data.

---

## HTTP is stateless
HTTP is stateless.

This means each request is treated independently unless the website uses something like cookies or sessions to remember the user.

Without cookies or sessions, the server would not naturally remember who I am between requests.

---

## URL
A URL is the address of a resource on the web.

Example:
https://example.com/login

Main parts:
- scheme: https
- host/domain: example.com
- path: /login

---

# HTTP Request Structure

## Main parts of a request
A request usually includes:
- method
- path
- HTTP version
- headers
- optional body

Example:
GET /login HTTP/1.1

This means:
- method = GET
- path = /login
- version = HTTP/1.1

---

## Method
The method tells the server what kind of action the client wants to perform.

The most important methods to know first are:
- GET
- POST

Other common methods:
- PUT
- PATCH
- DELETE

---

## GET
GET is used to request or retrieve data from the server.

GET usually asks for:
- a webpage
- an image
- search results
- public information

GET requests usually do not have a body in basic web browsing.

Examples:
- opening a homepage
- loading a profile page
- viewing a product page

Important idea:
GET should mainly retrieve data, not change important server-side state.

---

## POST
POST is used to send data to the server.

POST is often used when:
- submitting a login form
- creating something
- sending form input
- sending API data

POST requests often include a body.

Examples:
- sending username and password
- submitting a comment
- uploading form data

Important idea:
POST is commonly used for actions that send or create data.

---

## PUT
PUT is usually used to replace or fully update a resource.

Example:
Replacing all details of a stored record.

In many modern APIs, PUT means:
“replace this resource with the new version.”

---

## PATCH
PATCH is usually used to partially update a resource.

Example:
Changing only one field of a profile instead of replacing the whole thing.

PATCH often means:
“change part of this resource.”

---

## DELETE
DELETE is used to remove a resource.

Example:
Deleting a post, account item, or stored object.

---

# Headers

## What headers are
Headers are key-value pieces of extra information included in requests and responses.

Headers help describe:
- who is sending the request
- what type of content is involved
- session or cookie data
- how the client and server should handle the data

Headers are very important in web security because they often contain useful context.

---

## Common request headers

### Host
Shows the target domain.

Example:
Host: example.com

### User-Agent
Shows information about the browser or client.

Example:
User-Agent: Mozilla/5.0 ...

### Cookie
Contains cookies being sent by the browser to the server.

Example:
Cookie: sessionid=abc123

### Content-Type
Describes the format of the data being sent.

Example:
Content-Type: application/x-www-form-urlencoded
Content-Type: application/json

### Authorization
Used to send credentials or tokens in some applications and APIs.

---

# HTTP Response Basics

## Status code
A status code is a number in the response that tells the result of the request.

It helps the client understand what happened.

---

## Common status codes

### 200 OK
The request succeeded.

### 201 Created
A new resource was created successfully.

### 301 Moved Permanently
The resource has been permanently moved to a new location.

### 302 Found / Redirect
The client is being redirected to another location.

### 400 Bad Request
The request was malformed or invalid.

### 401 Unauthorized
Authentication is required or failed.

### 403 Forbidden
The server understood the request but refuses to allow access.

### 404 Not Found
The requested resource could not be found.

### 500 Internal Server Error
Something went wrong on the server side.

---

## Status code groups
Status codes are grouped by first digit:

- 1xx = informational
- 2xx = success
- 3xx = redirect
- 4xx = client-side issue
- 5xx = server-side issue

---

# Request Body

## What a body is
A body is the data sent with some requests.

Bodies are common in:
- POST
- PUT
- PATCH

Example uses:
- login form submission
- API JSON data
- profile updates

GET usually does not rely on a body in standard browser use.


