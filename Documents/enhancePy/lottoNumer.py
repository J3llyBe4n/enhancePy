import pymysql
import pandas as pd
import requests as re

class ConnectSQL:

    def ConnectDBServer(self):
        self.connection = pymysql.connect(host ='localhost', port=3306, user='root', passwd='test123', db='lotto')
        print("HI")

    def DisconnectDBServer(self):
        self.connection.close()
        print("bye")

class functionLotto(ConnectSQL):

    # 회차 정보 입력
    def insertRoundInfo(self):
        self.roundNum = int(input("insert round : "))
        print(self.roundNum)

    #db테이블 보기
    def viewRoundInfo(self):
        #self.connection = pymysql.connect(host ='localhost', port=3306, user='root', passwd='test123', db='lotto')
        cursor = self.connection.cursor()
        sql = 'select * from roundInfo where roundNumber = {}'.format(self.roundNum)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        print(df)

    #db 테이블 입력
    def storeRoundInfo(self):
        self.connection = pymysql.connect(host ='localhost', port=3306, user='root', passwd='test123', db='lotto')
        cursor = self.connection.cursor()
        sql = 'insert into roundInfo values({},{},{},{},{},{},{})'.format()

#lass callAPI():



#sql 서버 만들기


st = functionLotto()
st.ConnectDBServer()

st.insertRoundInfo()
st.viewRoundInfo()

#sql.DisconnectDBServer()
