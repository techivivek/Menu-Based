#!/usr/bin/python3

import cgi
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
to_email = form.getvalue('to_email')
subject = form.getvalue('subject')
message = form.getvalue('message')

# Your email credentials
from_email = 'enter your email'
password = 'enter your password'

def send_email(to_email, subject, message):
    try:
        # Setup the MIME
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the message to the MIME
        msg.attach(MIMEText(message, 'plain'))

        # Create SMTP session for sending the email
        server = smtplib.SMTP('smtp.gmail.com', 587)  # use Gmail with TLS
        server.starttls()  # enable security
        server.login(from_email, password)  # login with your email and password
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()

        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email. Error: {str(e)}"

# Send the email and get the result
result = send_email(to_email, subject, message)

print("Content-type:text/html")
print()
print("<html><body>")
print(f"<h2>{result}</h2>")
print("</body></html>")
