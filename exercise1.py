#!/usr/bin/env python

# This was the shebang line

from __future__ import print_function

# This is to make the print() function compatible with python 2

"""

Exercise 1: Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing 
three corresponding IP addresses). Print these three variables to standard output using a single
print statement.

Make your print statement compatible with both Python2 and Python3.

If you are using either Linux or MacOS make your program executable by 
adding a shebang line and
by changing the files permissions (i.e. chmod 755 exercise1.py).

"""

ip_addr = '10.200.36.14'
ip_addr2 = '10.200.36.15'
ip_addr3 = '10.200.36.16'

print(ip_addr, ip_addr2, ip_addr3)
