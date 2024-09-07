Open

#!/usr/bin/python3
print("content-type: text/html")
print ()
import subprocess
import cgi
form = cgi.FieldStorage()
cmd = form.getvalue("x")
value = cmd
if "date" in value:
output = subprocess.getoutput ("date")
print (output)
elif "path" in value:
output = subprocess.getoutput ("pwd")
print (output)
elif "site" in value:
output = subprocess.getoutput("curl http://192.168.43.99/vivek.html")
print (output)
elif "ip" in value:
output = subprocess.getoutput("ifconfig")
print (output)
elif "find" in value:
output = subprocess.getoutput("ps -aux | grep httpd")
print (output)
else:
print("this option is not available")

print("Go to previous page for more features")
