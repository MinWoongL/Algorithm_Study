# 2493_탑_transmission tower

# stack 문제 : 탑 방향 ->, 송신방향 <-
import sys

n = int(input())

tower_li = list(map(int, sys.stdin.readline().split()))

tower_stack = [tower_li[0]]  # 스택에 첫 타워 저장
tower_di = {tower_li[0]: 1}  # 특정높이타워의 위치를 기록하기 위해서 사용 (첫 타워 위치 1로 저장)
ans = [0]  # 첫 타워는 무조건 0 출력, 정답 리스트

for i in range(1, len(tower_li)):
    if tower_li[i] > tower_stack[-1]:  # 현재타워의 높이가 스택의 마지막타워보다 높을 때

        while tower_stack[-1] < tower_li[i]:  # 스택의 마지막 타워가 더 높아질 때 까지 pop연산
            tower_stack.pop()
            if len(tower_stack) == 0:  # 모든 스택이 사라지면 0 저장
                ans.append(0)
                break

        if len(tower_stack) != 0:  # 스택에 기록이 있으면 현재타워의 송신을 받는 타워 위치를 리스트에 저장
            ans.append(tower_di[tower_stack[-1]])

        tower_stack.append(tower_li[i])
        tower_di[tower_li[i]] = i+1

        # print(tower_stack)
        # print(tower_di)
    else:
        ans.append(tower_di[tower_stack[-1]])  # 현재타워 높이가 더 낮다면 스택의 마지막 타워 위치를 정답리스트에 추가
        tower_stack.append(tower_li[i]) 
        tower_di[tower_li[i]] = i + 1

for i in range(len(ans)):
    if i != (len(ans)-1):
        print(ans[i], end=' ')
    else:
        print(ans[i])
        # print(tower_stack)
        # print(tower_di)


'''
# 이 방법으로 틀림 stack을 활용 못함
print(0,end=' ')
for i in range(1,len(tower_li)):  # 6 9 5 7 4 8 3 일 때, 8은 9(2번째타워)에서 송신해야하는데 저장을 못해 7로 감
    if tower_li[i] < transtower:
        print(toweridx,end=' ')
    else:
        print(toweridx,end=' ')
        toweridx = i+1
'''


