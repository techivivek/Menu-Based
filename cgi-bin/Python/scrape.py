#!/usr/bin/env python3

import cgi
import requests
from bs4 import BeautifulSoup
import html

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
url = form.getvalue('url')

if url:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract specific data, for example, all paragraphs
        paragraphs = soup.find_all('p')
        content = "\n".join([p.get_text() for p in paragraphs])
        
        # Generate HTML response
        response_html = f"""
        <html>
        <head>
            <title>Website Scraper</title>
        </head>
        <body>
            <h1>Scraped Data from {html.escape(url)}</h1>
            <pre>{html.escape(content)}</pre>
        </body>
        </html>
        """
    except requests.RequestException as e:
        response_html = f"""
        <html>
        <head>
            <title>Website Scraper</title>
        </head>
        <body>
            <h1>Error</h1>
            <p>Could not retrieve data from {html.escape(url)}. Error: {html.escape(str(e))}</p>
        </body>
        </html>
        """
else:
    response_html = """
    <html>
    <head>
        <title>Website Scraper</title>
    </head>
    <body>
        <h1>Website Scraper</h1>
        <form method="post" action="/cgi-bin/scrape_website.py">
            <label for="url">Enter website URL:</label>
            <input type="text" id="url" name="url" required>
            <input type="submit" value="Scrape Website">
        </form>
    </body>
    </html>
    """

print(response_html)
