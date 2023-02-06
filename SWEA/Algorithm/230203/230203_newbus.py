# 새로운 버스 노선_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    avenue = {}
    for ttc in range(1, N+1):
        T, A, B = map(int, input().split())

        if T == 1:
            for j in range(A, B+1):
                if j in avenue.keys():
                    avenue[j] += 1
                else:
                    avenue[j] = 1
        elif T == 2:
            if A%2 == 0:
                for k in range(A, B + 1):
                    if k%2 == 0:
                        if k in avenue.keys():
                            avenue[k] += 1
                        else:
                            avenue[k] = 1
            else:
                for k in range(A, B + 1):
                    if k%2 == 1:
                        if k in avenue.keys():
                            avenue[k] += 1
                        else:
                            avenue[k] = 1
        else:
            if A%2 == 0:
                for l in range(A, B+1):
                    if l%4 == 0:
                        if l in avenue.keys():
                            avenue[l] += 1
                        else:
                            avenue[l] = 1
            else:
                for l in range(A, B+1):
                    if l%3 == 0 and l%10 != 0:
                        if l in avenue.keys():
                            avenue[l] += 1
                        else:
                            avenue[l] = 1

    max_value = 1
    for v in avenue.keys():
        if avenue[v] > max_value:
            max_value = avenue[v]
    print('#{} {}'.format(tc, max_value))
