#!/usr/bin/env python

# That was the shebang line

"""
Create three different variables: the first variable should use all lower case characters with
underscore ( _ ) as the word separator. The second variable should use all upper case characters
with underscore as the word separator. The third variable should use numbers, letters, and
underscores, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3

"""

from __future__ import print_function, unicode_literals

ipv6_addr1 = "2001:db8::1:1"
IPV6_ADDR2 = "2001:db8::1:2"
IpV6_addr3 = "2001:db8::1:3"

print()
print("Is variable1 equal to variable2?: {}".format(ipv6_addr1 == IPV6_ADDR2))
print("Is variable2 not equal to variable3?: {}".format(IPV6_ADDR2 != IpV6_addr3))
print()

print(type(ipv6_addr1))