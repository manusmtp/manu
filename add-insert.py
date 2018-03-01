#!/usr/bin/python

import cgi, cgitb 
from serverdb import insertRecord
#from serverdb import searchRecord
#try:
form = cgi.FieldStorage() 
server_name = form.getvalue('sname')
status = form.getvalue('status')
os = form.getvalue('os')
env = form.getvalue('ENV')
auth = form.getvalue('auth')
app = form.getvalue('app')
depend = form.getvalue('depend')
loc = form.getvalue('loc')
access = form.getvalue('access')
monit = form.getvalue('monit')
maintain = form.getvalue('maint')
frame = form.getvalue('frame')
backup = form.getvalue('backup')
insertRecord(server_name,status,os,env,auth,app,loc,depend,access,monit,maintain,frame,backup)
print "Content-type: text/html\n\n";
print ""
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>Server addition</title>"
print "</head>"
print "<body>"
print "<div><h3>server is added </div></h3>"
print "</body>"
print "</html>"

#except Exception, e:
#	print('Failed to upload to ftp: '+ str(e))
