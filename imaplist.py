#!/usr/bin/env python

import imaplib 

server = "outlook.office365.com"
user = "david.thornton@scalar.ca"
# pass = ">U#r5hu8,L8<"

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
    mylist = M.list()
except:
    print "M list failed : %s" % M.error
print "M list ok"
for item in mylist:
    for i in item:
        print "%s" % i
