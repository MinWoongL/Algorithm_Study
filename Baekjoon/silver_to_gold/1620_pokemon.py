# 1620_나는야포켓몬마스터_pokemon
# 번호와 포켓몬이름으로 서로 데이터를 불러올수 있어야한다 -> 각각 딕셔너리 만들기
import sys

N, M = map(int, input().split())

pdi1 = {}
pdi2 = {}
for i in range(1,N+1):
    s = sys.stdin.readline().strip()

    pdi1[s] = i
    pdi2[str(i)] = s  # 여기서 str로 감싸주지 않으면 나중에 해당 키값을 받을때 type이 달라 받아오지 못한다.


for j in range(M):
    quiz = sys.stdin.readline().strip()

    if quiz.isdigit():
        print(pdi2[quiz])
    else:
        print(pdi1[quiz])