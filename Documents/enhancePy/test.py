import requests as re

class LottoryNode:
    def __init__(self,LottoryNum, LottoryInfo):
        self.LottoryNum = LottoryNum
        self.LottoryInfo = LottoryInfo


class Lottory(LottoryNode):

    def logging_time(original_fn):
        import time
        from functools import wraps
        @wraps(original_fn)
        def wrapper(*args, **kwargs):
            start_time = time.process_time()
            result = original_fn(*args, **kwargs)

            end_time = time.process_time()
            print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time - start_time))
            return result

        return wrapper

    def __init__(self):
        self.num = self.inputCh()
        self.UrlList = self.UrlStore()
        self.FinalData = self.MakeValue()
        #self.printData()

    def inputCh(self):
        tempNum = int(input("insert number : "))
        return tempNum

    def UrlStore(self):
        baseUrl = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
        tmpUrl =[]

        for i in range(1, self.num +1):
            finalUrl = baseUrl + str(i)
            tmpUrl.append(finalUrl)

        return tmpUrl

    def MakeValue(self):
       # FinalData ={}

        for i in range(len(self.UrlList)):
            tmpNO = []
            tmpApi = re.get(self.UrlList[i])
            convertJson = tmpApi.json()

            #print(convertJson)
            for j in range(1,7):
                tmpNO.append(convertJson["drwtNo{}".format(j)])

        tmpNode =LottoryNode(str(i+1) + "회차 정보 :",tmpNO)
        print(tmpNode.LottoryInfo)
        print(tmpNode.LottoryNum)
        print(tmpNode)
        #print(tmpNode.LotteryNum)
        # FinalData[str(i+1) + "회차 정보 : "] = tmpNO

        return tmpNode

    def printData(self):
        for key, value in self.FinalData.items():
            print(key, value)


LotteryNodeAddr = []
lo = Lottory()

