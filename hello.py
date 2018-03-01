#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
from serverdb import searchRecord

form = cgi.FieldStorage() 
server_name = form.getvalue('server_name')
rows = searchRecord(server_name)
print "Content-type:text/html\r\n\r\n"

fname="header.html"
with open(fname, 'r') as fin:
    print fin.read()

for i in range(1,14):
	print "<td>%s</td>" % ( rows[i] )

fname="footer.html"
with open(fname, 'r') as fin:
    print fin.read()
