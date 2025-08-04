import stackDS
operators={"+":1,"-":1,"*":2,"/":2,"^":3}
def infix_to_postfix(expression):
    stack=stackDS.Stack(10)
    result=""
    for i in expression:
        if i not in operators:
            result=result+i
        else:
            if stack.is_empty() or operators[stack.top()]<operators[i]:
                stack.push(i)
            else:
                while not stack.is_empty() and operators[stack.top()]>=operators[i]:
                    popped=stack.pop()
                    result=result+popped
                stack.push(i)

    if not stack.is_empty():
        popped=stack.pop()
        result=result+popped
    
    return result

print(infix_to_postfix("a+b*c+d"))
