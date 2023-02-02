# 1일차_View_서울2반_이민웅


def view(nli):
    count_sum = 0
    cnt = 255
    for i in range(2, len(nli)-2):
        for j in range(i-2, i):
            if nli[j] > nli[i]:
                cnt = 0
                break
            else:
                if (nli[i] - nli[j]) < cnt:
                    cnt = nli[i] - nli[j]
        for k in range(i+1, i+3):
            if nli[k] > nli[i]:
                cnt = 0
                break
            else:
                if (nli[i] - nli[k]) < cnt:
                    cnt = nli[i] - nli[k]
        count_sum += cnt
        cnt = 255
    return count_sum


for i in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))

    print('#{} {}'.format(i, view(building)))



