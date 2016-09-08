#!/usr/bin/env python

# David Thornton northdot9@gmail.com
# https://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/
# https://tools.ietf.org/html/rfc3501

import imaplib 
import sys
import os
import pprint

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
pp = pprint.PrettyPrinter(indent=4)

server = "outlook.office365.com"
user = "david.thornton@scalar.ca"
# pass = ">U#r5hu8,L8<"
folder = "Sent Items"
limit = 10

print "connecting to server"
try:
    M = imaplib.IMAP4_SSL(server)
except:
    print "imap error: %s" % M.error

print "create imap object M ok"

try:
    M.LOGIN(user, '>U#r5hu8,L8<')
except:
    print "IMAL login error %s" % M.error

print "IMAP LOGIN OK"

try:
    M.select(folder)
except:
    print "Select folder %s failed : %s" % ( folder , M.error )
print "Select folder %s ok" % folder

#result, data = M.uid('search', None, "SENTSINCE 1-Jan-2015 SENTBEFORE 31-Dec-2015") # search and return uids instead
try:
    result, data = M.uid('search', None, '(SENTSINCE 1-Jan-2016)')
except:
    print "Search failed"

print "Result %s" % result
print ""

ids = data[0]

print "IDs"

for id in ids[0:10]:
    try:
        result, data = M.uid('fetch', id, '(UID RFC822.HEADER)')
    except:
        print "FETCH Error %s" % M.error
    print "result %s" % result
    headerstr = data[0][1]
    header = headerstr.split("\r\n")
    print "header"
    pp.pprint(header)

