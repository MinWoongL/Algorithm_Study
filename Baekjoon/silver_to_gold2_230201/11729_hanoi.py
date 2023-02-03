# 11729_하노이 탑 이동순서_Hanoi

# a 시작위치, c = 최종위치, b = 중간위치

def hanoi(n, li, a, b, c):
    sub_li = []  # 재귀로 넣어주는 hanoi 함수에 빈 리스트를 넣어주기 위해 생성
    # n = 1,2 일 때, 해당 이동순서를 리스트에 저장 후 반환
    if n == 1:
        li.append([a, c])
        return li
    elif n == 2:
        li.append([a, b])
        li.append([a, c])
        li.append([b, c])
        return li

    # 3단계로 나눠서 n-1 번째에 진행된 하노이탑 이동순서를 ans_li 에 저장

    ans_li = []
    ans = hanoi(n - 1, li, a, c, b)
    for v in ans:  # n-1 크기의 탑을 중간위치(b)에 이동
        ans_li.append(v)

    ans_li.append([a, c])  # n 번째 블럭을 최종위치(c)에 이동

    ans2 = hanoi(n - 1, sub_li, b, a, c)
    for v1 in ans2:  # n-1 크기의 탑을 중간위치(b)에서 최종위치(c)로 이동
        ans_li.append(v1)

    return ans_li


def cnt(n):  # 하노이탑의 이동순서를 계산하는 함수
    if n == 1:
        return 1
    else:
        return cnt(n - 1) + 2 ** (n - 1)


N = int(input())

move_li = []
count = cnt(N)

print(count)
last_li = hanoi(N, move_li, 1, 2, 3)
for v in last_li:
    print(*v)

