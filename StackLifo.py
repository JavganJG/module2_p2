class StackLifo():

    def __init__(self):
        self.__mystack = []
    

    def push(self,elem):
        self.__mystack.append(elem)
    def pop(self):
        if len(self.__mystack)>0:   
            return self.__mystack.pop()
        return None


stack=StackLifo()
print(stack._StackLifo__mystack)
print(stack.__dict__)
stack.push(9)
stack.push(2)
stack.push(7)
stack.push(4)
stack.push(8)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
