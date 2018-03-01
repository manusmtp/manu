#!/bin/python

import sqlite3
from sqlite3 import Error
from serverdb import searchRecord


class uServer:
	rowid =""
	title = ""
	status = ""
	os = ""
	env = ""
	auth = ""
	app = ""	
	location = ""
	depen  = "" 
	acess = ""
	monit = ""
	maintain = ""
	frame = ""
	backup = "" 
	
	def __init__(self,rowid,title,status,os,env,auth,app,location,depen,acess,monit,maintain,frame,backup):
		self.rowid = rowid
		self.title = title
		self.status = status
		self.os = os
		self.env = env
		self.auth = auth
		self.app = app
		self.location = location
		self.depen = depen
		self.acess = acess
		self.monit = monit
		self.maintain = maintain
		self.frame = frame
		self.backup = backup

	def printServer(self):
		print "--"
		print  self.rowid
		print  self.title
		print  self.status	
	
def addServer(self,title,status,os,env,auth,app,location,depen,acess,monit,maintain,frame,backup):
		title = self.title
		status = self.status
		os = self.os
		env = self.env
		auth = self.auth
		app = self.app
		location = self.location
		depen = self.depen
		acess  = self.acess
		monit = self.monit
		maintain = self.maintain
		frame = self.frame
		backup = self.backup
		print "completed the assi"
		
def searchServer():
		sname = raw_input("server name::")
		row = searchRecord(sname)
		instance = uServer(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
		#print "instance created"
		#instance.printServer()
			
		 		
			
	
def deleteServer(self):
		pass

def updateServer(self):
		pass
	

#o1 =  uServer()
#o1.addServer("lx000330","","","","","","","","","","","","")
#searchServer()
#print "server returned " 
