#db creation
import mysql.connector
from mysql.connector import errorcode
DB_NAME = 'emp'
TABLES = {}
TABLES['employees'] = ("CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

TABLES['departments'] = (
    "CREATE TABLE `departments` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `dept_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
    ") ENGINE=InnoDB")

cn = mysql.connector.connect(user='root', password='root') #connection for database creation without 'database name'
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
#set the database end

# creating tables
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

# creating tables end

set_database(DB_NAME)
create_tables(TABLES)

