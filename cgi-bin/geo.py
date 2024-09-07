#!/usr/bin/env python3

import cgi
import cgitb
import json
import requests

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

# Parse the query parameters
form = cgi.FieldStorage()
address = form.getvalue("address")

# Define your Google Maps API key
API_KEY = 'enter your map api'
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

# Function to get coordinates
def get_coordinates(address):
    response = requests.get(GEOCODE_URL, params={
        'address': address,
        'key': API_KEY
    })
    return response.json()

# Get coordinates for the provided address
result = get_coordinates(address)

# Output the result as JSON
print(json.dumps(result))
