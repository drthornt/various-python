#!/usr/bin/env python

# #!/usr/bin/python

from lxml import html
import requests
import re
import dns.resolver
import sys

res = dns.resolver
url = 'https://cygwin.com/mirrors.html'
page = requests.get(url)
tree = html.fromstring(page.content)

links = tree.xpath('//a')

mydict = {}

for link in links:
    myatt = link.attrib
    if "href" in link.attrib:
        href = link.attrib["href"]
    else:
        print "NO HREF"
        continue
    print link.text  , href
    mo = re.search(r'(https|http|rsync|ftp):\/\/(.*)', href)
    if mo:
        # print "||", link.text , "||" , href
        proto =  mo.group(1)
        # print "\t", mo.group(2)
        ( host , slash , path ) = mo.group(2).partition('/')
        # print "\t", slash + path
        mydict[host] = {}
        mydict[host][proto] = slash + path
        mydict[host]['dns'] = {}
    else:
        print "Bad href (didn\'t parse)", href




for key,val in mydict.items():
    print key
    print val

    

