#querying data
import datetime
import mysql.connector
cn = mysql.connector.connect(user='root', database='emp',password='root',host='127.0.0.1') #creating connection
cr = cn.cursor() #handle structure (like dataatapter)

query = ("SELECT * FROM employees")
cr.execute(query)
for (en,dob,fn,ln,g,hd) in cr: #here en,dob,fn,ln,g,hd are the variables respectively to the fields in the employees table
  print("Employee No {0} of {2} {3} was born on {1:%d %b %Y} as {4} \n Now hired for the job on {5:%d %b %Y} \n".format(en, dob, fn, ln, g, hd))
cr.close() #closing the cursor
cn.close() #closing the connection
