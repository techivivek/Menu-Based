#!/usr/bin/python3

import subprocess

print('content-type: text/html')
print('\n')

cmd="sudo docker run -dit centos:7"

o=subprocess.getoutput(cmd)
print(o)
