#!/usr/bin/env python3

# feed this a cisco's "ip route" and it will output a dot file fit for passign to graphviz.

from lxml import html
import requests
import re
import dns.resolver
import sys

input_file  = sys.argv[1]

print "sooper"

filereader = open( input_file , 'r' )
for line in filereader:
    print line.strip()
filereader.close()

