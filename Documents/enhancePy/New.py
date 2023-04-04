import pymysql
import mysql.connector
import pandas as pd
import requests as re
from tabulate import tabulate


#DBMS 상태 처리 class
class ConnectSQL():

    #db 연결
    def ConnectDBServer(self):
        self.connection = mysql.connector.connect(option_files='my.conf')
        self.cursor = self.connection.cursor()
        print("-----------------------------------------------")
        print("HI SQL")
        print("-----------------------------------------------")


    #db 연결해제
    def DisconnectDBServer(self):
        self.connection.close()
        print("-----------------------------------------------")
        print("bye SQL")
        print("-----------------------------------------------")

#api 데이터 처리 class
class Api():

    #Api request 하여 받은 data을 list에 적재하여, 해당 list의 인덱싱하기위해 init
    def __init__(self):
        self.tmpData = []

    # request 할 url 적재
    def storeApiUrl(self):
        self.tmpRoundNumber = int(input("회차 정보를 입력하라 : "))
        baseUrl = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
        self.tmpUrl = baseUrl + str(self.tmpRoundNumber)

    # api url을 통해 원하는 data format으로 변환
    def getValueApi(self):
        tmpApi = re.get(self.tmpUrl)
        self.convertJson = tmpApi.json()

    # url을 통해서 로또 번호를 리스트로 적재
    def storeData(self):
        for i in range(1,7):
            self.tmpData.append(self.convertJson["drwtNo{}".format(i)])


#실제 api를 data를 파싱받아 처리하는 class
class FunctionMixin(ConnectSQL, Api):

    #db 들여다보기
    def viewDB(self):

        # DB서버 열어주기
        self.ConnectDBServer()
        sql = 'select * from roundInfo'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        df = pd.DataFrame(result)

        #print(df.columns)

        df.columns = ['회차번호', '1번째', '2번째', '3번째', '4번째', '5번째', '6번째']
        #print(df)
        print(tabulate(df, headers= 'keys', tablefmt ='pretty', showindex=False))

       # print(df.to_string(index=False))

        # DB서버 닫아주기
        self.DisconnectDBServer()

    #db 박아넣기
    def insertDB(self):

        #DB 서버 열어주기
        self.ConnectDBServer()

        self.storeApiUrl()
        self.getValueApi()
        self.storeData()

        #tmpData = [200,1,2,4,5,6,7]
        sql = 'insert into roundInfo values(%d,%d,%d,%d,%d,%d,%d)' %(self.tmpRoundNumber,
                                                                     self.tmpData[0],
                                                                     self.tmpData[1],
                                                                     self.tmpData[2],
                                                                     self.tmpData[3],
                                                                     self.tmpData[4],
                                                                     self.tmpData[5])
        self.cursor.execute(sql)
        self.connection.commit()
        print("완료")

        #DB 서버 닫아주기
        self.DisconnectDBServer()

    #db 지우기
    def deleteDB(self):

        #DB 서버 열어주기
        self.ConnectDBServer()
        deleteRound = int(input("지울 회차를 입력하라 : "))
        sql = 'delete from roundInfo where roundNumber = %d' %deleteRound
        #print(sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print("완료")

        #DB서버 닫아주기
        self.DisconnectDBServer()



# 번호 입력 ex 1. 회차 정보 보기 / 2. 회차 정보 입력 / 3. 회차정보 삭제       // 시키는 main
#1번 눌럿을때, 보여주기!
#클래스구성 노트보기

if __name__ == '__main__':

    fu = FunctionMixin()
    print("원하는 번호를 입력하세요\n 1. 보기 2. 삽입, 3. 삭제 ")
    num = int(input("insert number"))

    if num == 1:
        print("회차 정보 보기 ")
        fu.viewDB()

    elif num == 2:
        print("원하는 회차 정보 입력 하기 위해서 번호 한번 더 받기")
        fu.insertDB()

    elif num == 3:
        print("회차 정보 삭제 하기 위해서 번호 한번 더 받기 ")
        fu.deleteDB()