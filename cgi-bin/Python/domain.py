#!/usr/bin/env python3

import cgi
import whois
import html

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
domain = form.getvalue('domain')

if domain:
    try:
        domain_info = whois.whois(domain)
        response = f"""
        <html>
        <head>
            <title>Domain Finder</title>
        </head>
        <body>
            <h1>Domain Information for {html.escape(domain)}</h1>
            <pre>{html.escape(str(domain_info))}</pre>
        </body>
        </html>
        """
    except Exception as e:
        response = f"""
        <html>
        <head>
            <title>Domain Finder</title>
        </head>
        <body>
            <h1>Error</h1>
            <p>Could not retrieve information for {html.escape(domain)}. Error: {html.escape(str(e))}</p>
        </body>
        </html>
        """
else:
    response = """
    <html>
    <head>
        <title>Domain Finder</title>
    </head>
    <body>
        <h1>Domain Finder</h1>
        <form method="post" action="/cgi-bin/domain_finder.py">
            <label for="domain">Enter domain name:</label>
            <input type="text" id="domain" name="domain" required>
            <input type="submit" value="Find Domain">
        </form>
    </body>
    </html>
    """

print(response)
