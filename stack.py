
mystack=[]


def push(elem):
    mystack.append(elem)
    
def pop():
    if(mystack.count==0):
        return None
    else:
        elem = mystack[-1]
        mystack.pop(-1)
        return elem
