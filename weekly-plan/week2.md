Week 2 theme
 * Learn HTTP and cookies/sessions properly from start to finish
   End goal for the week
 	By the end of the week, you should be able to:
	explain what HTTP is
	explain request vs response
	identify common methods
	identify common status codes
	read headers
	understand what cookies are
	understand what sessions are
	inspect all of this in browser dev tools and Burp
	write clean notes about it

Monday — HTTP foundation 1

	Focus only on:

		what HTTP is
		what a client is
		what a server is
		what a request is
		what a response is
	Tasks
		read and write notes on:
		HTTP, client, server, request, response
		open browser dev tools
		inspect 3 requests
		for each one, identify:
		request, response
		
Tuesday — HTTP foundation 2

	Focus only on:

		methods
		status codes
		URL/path
		headers
		Learn these properly

	Methods:

		GET
		POST

	Status codes:

		200
		301/302
		403
		404
		500

	Headers:

		Host
		User-Agent
		Cookie
		Content-Type
		Tasks
		inspect more requests in browser dev tools
		find: method, path, headers
		
Wednesday — HTTP practice day

	Focus only on:

		reading requests fluently
		Tasks
		open Burp
		intercept requests
		for each captured request, identify:
		method
		path
		host
		headers
		do this multiple times until it starts feeling repetitive


Thursday — Cookies foundation

	Focus only on:

		what cookies are
		where cookies appear
		why cookies exist
	Tasks
		learn:
		cookie = small data stored in browser
		cookies are sent with requests
		cookies help maintain state
		inspect cookies in browser dev tools
		inspect cookies in Burp
		write what a cookie looks like
	
Friday — Sessions foundation

	Focus only on:

		what sessions are
		why sessions exist
		how sessions connect to cookies
		Learn this clearly
		HTTP is stateless
		sessions help websites remember users
		session IDs are often stored in cookies
		if session handling is weak, security problems happen
	Tasks
		inspect a site where you can observe cookies before and after page changes
		write what changed and what stayed the same
		explain in your own words how cookies and sessions connect

Saturday — Deep practice day

	Focus only on:

		putting HTTP + cookies + sessions together
		Tasks

		Do 3 full practice rounds:

		capture a request
		identify method
		identify headers
		identify cookie
		note status code
		explain what is happening
