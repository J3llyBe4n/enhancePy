import pymysql
import pandas as pd
import requests as re




connection = pymysql.connect(host ='localhost', port=3306, user='root', passwd='test123', db='sqldb')
cursor = connection.cursor()
sql = 'select * from usertb1'
cursor.execute(sql)

result = cursor.fetchall()
connection.close()
df = pd.DataFrame(result)
print(df)

