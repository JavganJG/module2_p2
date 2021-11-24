import StackLifo as SL

class StackSumLifo(SL.StackLifo):
    def __init__(self):
        super().__init__()
        self.__sum = 0

    def getSum(self):
        return self.__sum

    def push(self, elem):
        super().push(elem)
        self.__sum += elem

    def pop(self):
        elem = super().pop()
        if elem != None:
            self.__sum -= elem
        return elem

objsum = StackSumLifo()

objsum.push(7)
print("Now: "+str(objsum.getSum()))
objsum.push(2)
print("Now: "+str(objsum.getSum()))
objsum.push(1)
print("Now: "+str(objsum.getSum()))
objsum.push(48)
print("Now: "+str(objsum.getSum()))


print(objsum.pop())
print("Now: "+str(objsum.getSum()))
print(objsum.pop())
print("Now: "+str(objsum.getSum()))
print(objsum.pop())
print("Now: "+str(objsum.getSum()))
print(objsum.pop())
print("Now: "+str(objsum.getSum()))
print(objsum.pop())
