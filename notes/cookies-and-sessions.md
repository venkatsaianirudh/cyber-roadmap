# Cookies and Sessions

## Why this topic matters
HTTP is stateless.

That means each request is separate by default. A server does not naturally remember who I am from one request to the next.

Cookies and sessions are two of the main ways websites keep track of users across multiple requests.

Without them, a website would treat each request like it came from a new visitor.

---

## Cookie
A cookie is a small piece of data stored in the browser.

The server can send a cookie to the browser, and the browser can send it back in later requests.

Cookies help the website keep track of information between requests.

Cookies are usually sent in HTTP headers.

---

## What cookies are used for
Cookies are commonly used for:
- login state
- session tracking
- user preferences
- shopping carts
- analytics or tracking

Not every cookie is a login cookie. Some are only for settings or tracking.

---

## How cookies work
Basic flow:
1. The browser sends a request to the server.
2. The server responds and may include a cookie.
3. The browser stores that cookie.
4. On later requests, the browser sends the cookie back.

This helps the server recognize something about the client.

---

## Cookie in HTTP
A server usually sends a cookie with a response header like:

Set-Cookie: sessionid=abc123

Later, the browser may send it back in a request header like:

Cookie: sessionid=abc123

This is one of the most important things to notice in Burp or browser dev tools.

---

## Cookie structure
A cookie usually has:
- a name
- a value
- optional attributes

Example idea:
sessionid=abc123

Here:
- cookie name = sessionid
- cookie value = abc123

---

## Common cookie attributes

### Secure
The cookie should only be sent over HTTPS.

This helps reduce the chance of it being exposed over insecure connections.

### HttpOnly
The cookie should not be accessible through JavaScript.

This helps reduce some risks from client-side attacks such as certain XSS situations.

### SameSite
Helps control when cookies are sent in cross-site requests.

This is important for reducing some CSRF-related risks.

### Expires / Max-Age
Controls how long the cookie lasts.

---

## Session
A session is a server-side way of remembering a user.

The session usually stores user-related state on the server, while the browser keeps only a session identifier.

A session often depends on a cookie that contains the session ID.

---

## Session ID
A session ID is a unique value that links the browser to a server-side session.

Instead of storing all important state inside the browser, the browser often stores only the session ID.

The server uses that ID to find the session data.

Example idea:
- browser stores: sessionid=abc123
- server maps abc123 to a user session

---

## How sessions work
Basic flow:
1. User visits a site.
2. Server creates a session or prepares one after login.
3. Server sends a session ID to the browser, usually in a cookie.
4. Browser sends the session ID back on future requests.
5. Server uses the session ID to remember the user.

This is how a website can keep someone logged in across multiple pages.

---

## Cookies vs sessions
A cookie is data stored in the browser.

A session is usually data stored on the server.

A cookie can exist without a session.
A session often uses a cookie to work.

Simple way to think about it:
- cookie = what the browser stores
- session = what the server remembers

---

## Session cookie
A session cookie is a cookie used to identify a session.

It often contains a session ID.

This is one of the most important cookies in web security because if someone steals it, they may be able to act like the logged-in user.

---

## Why cookies matter in security
Cookies matter because they can affect:
- authentication
- user tracking
- session state
- access to accounts

If cookies are weak, exposed, or misused, attackers may be able to:
- impersonate users
- hijack sessions
- abuse login state
- bypass intended protections in some cases

---

## Why sessions matter in security
Sessions matter because they are how the server keeps track of a user’s authenticated state.

If session handling is weak, problems can happen such as:
- session hijacking
- session fixation
- poor logout handling
- insecure session IDs
- predictable session behavior

I do not need to master all of those attacks yet, but I need to understand that session handling is a major security area.

---

## Session hijacking
Session hijacking means an attacker gets access to another user’s valid session identifier and uses it.

If a website trusts that session ID, the attacker may be treated as that user.

This is why protecting session cookies is important.

---

## Session fixation
Session fixation is when an attacker tries to force or influence which session ID a user uses.

If the application handles sessions badly, that can become dangerous.

For now, I only need to know the concept exists.

---

## Why HTTP being stateless matters
HTTP does not remember users by itself.

Cookies and sessions are solutions to that problem.

This is why learning HTTP, cookies, and sessions together makes sense.

---

## What to look for in Burp or DevTools
When inspecting traffic, I should look for:
- whether the response sets a cookie
- whether the request sends a cookie
- what the cookie name is
- whether the cookie appears stable across requests
- whether the cookie has security attributes like Secure or HttpOnly
- whether login state seems tied to that cookie

---

## What to observe during practice
When I capture traffic, I should ask:
- Did the server send a Set-Cookie header?
- Is the browser sending a Cookie header back?
- Does the cookie appear after login or before login?
- Does the cookie change after login?
- Does the site seem to remember the user because of that cookie?

These questions help me connect raw HTTP to actual user state.

---

## Example flow
Example:
1. I visit a website.
2. The server responds and sets a cookie.
3. My browser stores it.
4. I click another page.
5. My browser sends the cookie back.
6. The server recognizes the session and responds accordingly.

That is the practical pattern I want to notice.

---

## Cookie security ideas to remember
Important ideas:
- login-related cookies are sensitive
- Secure helps protect cookies in HTTPS use
- HttpOnly helps reduce some JavaScript access risks
- SameSite helps reduce some cross-site abuse cases
- session cookies should be treated as valuable

---

## Easy difference summary
- Cookie = stored in browser
- Session = stored on server
- Session ID = value that links browser to server-side session
- Session cookie = cookie carrying the session ID

