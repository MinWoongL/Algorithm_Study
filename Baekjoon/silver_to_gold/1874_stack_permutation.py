# 1874_스택수열

# 다른풀이 찾아보기
import sys

n = int(input())

nli = [i for i in range(1,n+1)]
stack = [] # 스택을 저장할 리스트
pushpopli = [] # push, pop 기호를 저장할 리스트 (+,-)
highnum = 0 # 저장한 가장 큰 숫자 기록
for i in range(n):
    num = int(input())
    if len(stack) == 0: # 첫 숫자라면 해당 숫자까지 push후 pop
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
        if stack[-1] == num: # 입력받은 숫자가 스택의 마지막에 있으면 pop
            stack.pop()
            pushpopli.append('-')
            #print(stack)
            #print(pushpopli)
        else:
            if num < stack[-1]: # 입력받은 숫자가 스택의 마지막수보다 작으면 불가능
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




