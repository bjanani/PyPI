#coding for proper database connection#

import mysql.connector
from mysql.connector import errorcode
try:
 cn=mysql.connector.connect(user='root',host='127.0.0.1',password='root',database='test')
except mysql.connector.Error as err:
 if err.errno==errcode.ER_ACCESS_DENIED_ERROR:
   print("something is wrong with tour username or password")
 elif err.errno==errorcode.ER_BAD_DB_ERROR:
   print("databse does not exists")
 else:
   print(err)
else:
 cn.close()
   
