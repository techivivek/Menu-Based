#!/usr/bin/env python3

import os
import cgi
import cgitb
from twilio.rest import Client

cgitb.enable()

# Twilio credentials
account_sid = "enter your sid "
auth_token = "enter your token"
twilio_phone_number = "enter your twillio no"

print("Content-Type: text/plain\n")

form = cgi.FieldStorage()

if "to" in form and "message" in form:
    to_number = form["to"].value
    message_body = form["message"].value

    try:
        # Create Twilio client
        client = Client(account_sid, auth_token)

        # Send WhatsApp message
        message = client.messages.create(
            from_='whatsapp:' + twilio_phone_number,
            body=message_body,
            to='whatsapp:' + to_number
        )

        print(f"WhatsApp message sent successfully. Message SID: {message.sid}")
    except Exception as e:
        print(f"Error: {str(e)}")
else:
    print("Missing parameters. Please provide 'to' and 'message'.")
