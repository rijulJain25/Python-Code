import mysql.connector as c
conn = c.connect(host = 'localhost', user ='root', passwd = 'Ram#1212')
if conn.is_connected():
    print('connection with database established')
else:
    print('unable to connect to the database')
