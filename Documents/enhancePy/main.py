import requests as re

class Lottory:

    storeList =[]
    num= 0
    tempNum = 0

    def inputCh(self):
        tempNum = int(input("insert number : "))
        return tempNum

    def printF(self, tempNum1):
        print(tempNum1)

    def callUrlByAPI(self):
        for i in range(1, self.tempNum+1):
            finalUrl = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + str(i)
            print(finalUrl)
            self.findLottoryNumber(finalUrl)

    def findLottoryNumber(self, finalUrl):
        getJson = re.get(finalUrl)
        tempResult = getJson.json()
        print(tempResult)

#클래스 생성
lo = Lottory()

#입력값 받기
lo.inputCh()

#url구하기
lo.callUrlByAPI()






'''
num = int(input("insert 차수 : "))

for i in range(1, num+1):
    getJson = re.get(baseurl + str(i))
    #print(getJson)
    result = getJson.json()
    no1Num =result["drwtNo1"]
    tempList = []

    tempList.append(no1Num)
    print(tempList)

'''