# 1874_스택수열
import sys

n = int(input())

nli = [i for i in range(1,n+1)]
stack = []
pushpopli = []
highnum = 0
for i in range(n):
    num = int(input())
    if len(stack) == 0:
        for j in range(highnum, num):
            stack.append(nli[j])
            pushpopli.append('+')
            #print(stack)
        stack.pop()
        #print(stack)
        pushpopli.append('-')
        highnum = num
        #print(pushpopli)
    else:
        if stack[-1] == num:
            stack.pop()
            pushpopli.append('-')
            #print(stack)
            #print(pushpopli)
        else:
            if num < stack[-1]:
                print('NO')
                pushpopli.clear()
                break
            else:
                for k in range(highnum, num):
                    stack.append(nli[k])
                    pushpopli.append('+')
                    #print(stack)
                stack.pop()
                #print(stack)
                pushpopli.append('-')
                highnum = num
                #print(pushpopli)
if pushpopli:
    for v in pushpopli:
        print(v)




