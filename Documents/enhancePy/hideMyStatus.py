import pymysql
import mysql.connector

cnx = mysql.connector.connect(option_files='my.conf')

print(cnx)
cnx.close()