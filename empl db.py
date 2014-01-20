 #A PYTHON PROJECT FOR EMPLOYEE DATABASE#
 
 import mysql.connector
try:
  cn = mysql.connector.connect(user='root', host='127.0.0.1', password='vimaljanu', database='emp')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
  else:
    print(err)
else:
  cn.close()
  #db creation
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
DB_NAME = 'emp'
#DDL (Data Definition Language) statements
TABLES = {}
TABLES['empl'] = (
    "CREATE TABLE `empl` ("
    "  `emp_no` int(11), 
    "  `first_name` varchar(16),
    "  `last_name` varchar(16), 
    "  `gender` enum('M','F'),
    "  `hire_date` date ")

TABLES['dept'] = (
    "CREATE TABLE `dept` ("
    "  `dept_no` int(4),
    "  `dept_name` varchar(40)")

cn = mysql.connector.connect(user='root', password='vimaljanu') #connection for database creation without 'database name'
cr = cn.cursor() #cursor (handle structure

#database creation function
def create_database(pcr):
    try:
        pcr.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
# database creation function end

#set the database
def set_database(dbname):
    try:
        cn.database = dbname
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cr) # if failed to set it will call
            cn.database = dbname
        else:
            print(err)
            exit(1)
def create_tables(tbl):
    for name, ddl in tbl.items():
        try:
            print("Creating table {}: ".format(name), end='')
            cr.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
    cr.close()
    cn.close()
	#inserting the records to the table
import mysql.connector
from datetime import date, datetime, timedelta
#host='127.0.0.1' is mentioned the local system ip.
#If you want to connect another system database, mention the IP Address of the System
#example: (user='root' password='root' host='192.168.1.10' database='dbname')
cn = mysql.connector.connect(user='root', database='emp',password='vimaljanu',host='127.0.0.1') #creating connection
cr = cn.cursor() #handle structure (like dataatapter)
tomorrow = datetime.now().date() + timedelta(days=1)
query="INSERT INTO empl(emp_no,first_name, last_name, ,gender,hire_date) VALUES('{}','{}','{}','{}','{}')".format("Arun","Kumar",tomorrow,'M')
cr.execute(query)
emp_no = cr.lastrowid
#we retrieve the newly inserted value for the emp_no column (an AUTO_INCREMENT column) using the lastrowid property of the cursor object.
print("We Inserted the Employee Number of {0} ".format(emp_no))

# you must commit the data after a sequence of INSERT, DELETE, and UPDATE statements.
# Make sure data is committed to the database
cn.commit()
cr.close() #closing the cursor
cn.close() #closing the connection
#querying data
import datetime
import mysql.connector
cn = mysql.connector.connect(user='root', database='emp',password='vimaljanu',host='127.0.0.1') #creating connection
cr = cn.cursor() #handle structure (like dataatapter)

query = ("SELECT * FROM empl")
cr.execute(query)
for (en,dob,fn,ln,g,hd) in cr: #here en,dob,fn,ln,g,hd are the variables respectively to the fields in the employees table
  print("Employee No {0} of {2} {3} was born on {1:%d %b %Y} as {4} \n Now hired for the job on {5:%d %b %Y} \n".format(en, dob, fn, ln, g, hd))
cr.close() #closing the cursor
cn.close() #closing the connection
import os
os.system('cls')
import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', database='emp', password='vimaljanu')
ch=""
while ch!="0":
    ch=input("Enter Option 1 to continue 0 to stop 2 to clear: ")
    if ch=="2":
        os.system('cls')
    cursor = cnx.cursor()
    query = ("SELECT * from empl")
    cursor.execute(query)
    print("+ {} + {} +".format("-"*10,"-"*20))
    print("| {:^10} | {:^20} |".format("employeeID", "EmployeeName"))
    print("+ {:<5} | {:>20} +".format("-"*10,"-"*20))
    for (e,n) in cursor:
        b=str(e)
        d=b.zfill(4)
        print("| {:>10} | {:<20} |".format(d, n))
    print("+ {} + {} +".format("-"*10,"-"*20))
    cursor.close()
cnx.close()
#print("{2:d10}".format(10))
import os
os.system('cls')
import mysql.connector
cnx = mysql.connector.connect(user='root', database='emp', password='vimaljanu')
ch=""
while ch!="0":
    ch=input("Enter Option 1 to continue 0 to stop 2 to clear: ")
    if ch=="2":
        os.system('cls')
    elif ch=="1":
        cursor = cnx.cursor()
        query = ("SELECT * from empl")
        cursor.execute(query)
        print("+ {} + {} +".format("-"*10,"-"*20))
        print("| {:^10} | {:^20} |".format("employeeID", "EmployeeName"))
        print("+ {:<5} | {:>20} +".format("-"*10,"-"*20))
        for (e,n) in cursor:
            b=str(e)
            d=b.zfill(4)
            print("| {:>10} | {:<20} |".format(d, n))
        print("+ {} + {} +".format("-"*10,"-"*20))
cursor.close()
cnx.close()
#print("{2:d10}".format(10))



set_database(DB_NAME)
create_tables(TABLES)


