# 14425_문자열집합_wordset
# 숫자카드 문제와 동일하게 dict이용하여 탐색속도를 줄이는게 관건
# sys module을 이용하여 for 문 안의 input을 최대한 줄이는것도 좋다.
N, M = map(int, input().split())

sli = {}
count = 0
for i in range(N):
    s = input()
    sli[s] = 0

for j in range(M):
    s = input()
    if s in sli.keys():
        count += 1

print(count)
