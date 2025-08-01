import stackDS
opening=["(","[","{"]
closing=[")","]","}"]

def check(expression):
    stack=stackDS.Stack(len(expression))
    for i in expression:
        if i in opening:
            stack.push(i)
        elif i in closing:
            last=stack.pop()
            if closing.index(i)!=opening.index(last):
                return False
    if stack.is_empty():
        return True
    else:
        return False

print(check("(1+3{6-7[2-1])}"))

