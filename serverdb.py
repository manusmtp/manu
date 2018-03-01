#!/bin/python
 
import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
  
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 

 
def dbconnect():
  #server name without path since already directed to this dir
    database = "/home/apache/server_inventory.db"
    # create a database connection
    conn = create_connection(database)
    return conn

def insertRecord(server_name,status,os,env,auth,app,loc,depend,access,monit,maintain,frame,backup):
	conn = dbconnect()
        with conn:
                cur = conn.cursor()
                cur.execute('insert into server_inventory(title,status,os,env,auth,app,location,depen,acess,monit,maintain,frame,backup) values \
		(?,?,?,?,?,?,?,?,?,?,?,?,?)' , (server_name,status,os,env,auth,app,loc,depend,access,monit,maintain,frame,backup))
	        #print("record is inserted successfully"	)
		#return None


def deleteRecord():
	pass	

def searchRecord(sname):
	conn = dbconnect()
	with conn:
		cur = conn.cursor()
		cur.execute("SELECT rowid,* FROM server_inventory where title='%s'"  % (sname))
		row = cur.fetchone()
		return row	
			


def dbtofile():
	conn = dbconnect()
	fname = "systema.txt"
        with open(fname, 'a+') as fin:
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM server_inventory")
                eachrow = cur.fetchall()
		for record in eachrow:
    			print record[0] + ":" + record[1] + ":" + record[2] + ":" + record[3] + ":" + record[4] + ":" + record[5] + ":" + record[6] + ":" + record[7] + 			record[8] + ":" + record[9] + ":" + record[10] + ":" + record[11] + ":" + record[12] + ":" + record[13]  

server_name,status,os,env,auth,app,loc,depend,access,monit,maintain,frame,backup="test1","test1","test1","test1","test1","test1","test1","test1","test1","test1","test1","test1","test1"

#insertRecord(server_name,status,os,env,auth,app,loc,depend,access,monit,maintain,frame,backup)
