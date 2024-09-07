#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()  # for debugging

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
query = form.getvalue("query")

if query:
    # Redirect to Google search results
    print(f'<html><head><meta http-equiv="refresh" content="0;url=https://www.google.com/search?q={query}"></head><body></body></html>')
else:
    # Display the search form
    print('''
        <html>
        <head>
            <title>Google Search</title>
        </head>
        <body>
            <h1>Google Search</h1>
            <form method="get" action="/cgi-bin/google_search.py">
                <input type="text" name="query" placeholder="Search Google...">
                <input type="submit" value="Search">
            </form>
        </body>
        </html>
    ''')
