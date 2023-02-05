# E_Binary Inversions
import sys

T = int(input())

for tc in range(T):
    n = int(input())
    nli = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    cnt2 = 0
    if len(nli) == 1:
        print(0)
    else:
        nli_one = [nli[i] for i in range(n)]
        nli_zero = [nli[i] for i in range(n)]
        # 가장 앞쪽의 0을 1로 바꿔주면 해당 경우를 nli_one에 저장해주고 break
        while cnt == 0:
            for i in range(n):
                if nli_one[i] == 0:
                    nli_one[i] = 1
                    cnt += 1
                    break
            break
        # 가장 뒷쪽의 1을 0으로 바꿔주면 nli_zero에 저장해주고 break
        while cnt2 == 0:
            for j in range(n - 1, -1, -1):
                if nli_zero[j] == 1:
                    nli_zero[j] = 0
                    cnt2 += 1
                    break
            break

        ans1 = 0  # 0을 1로 바꿔준 경우 순서쌍의 수
        ans2 = 0  # 1을 0으로 바꿔준 경우 순서쌍의 수
        ans3 = 0  # 아무것도 바꾸지 않은경우 순서쌍의 수
        stack = []
        for i in range(n):  # 1을 스택에 쌓아주면서 0이 나올때마다 스택에 쌓인 1의 수만큼 ans1 ++
            if nli_one[i] == 1:
                stack.append(1)
            else:
                if stack:
                    ans1 += len(stack)
        stack.clear()

        for k in range(n):
            if nli_zero[k] == 1:
                stack.append(1)
            else:
                if stack:
                    ans2 += len(stack)
        stack.clear()

        for num in range(n):
            if nli[num] == 1:
                stack.append(1)
            else:
                if stack:
                    ans3 += len(stack)

        print(max(ans1, ans2, ans3))

