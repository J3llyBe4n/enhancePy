class A:
    tmpList = [1,2,3]

    def printA(self):
        print("classa")

class B:
    tmpListB = [4,5,6]

    def printB(self):
        print("classB")

class C(A,B):

    def printC(self):
        print("class C")

    def updateB(self):
        self.tmpListB.append(5)

    def printBB(self):
        print(self.tmpListB)

if __name__ == "__main__":

        ci = C()
        ci.updateB()
        ci.printBB()