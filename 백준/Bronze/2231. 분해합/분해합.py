def generator(N):
    g_li = []
    for i in range(1,N):  # N보다 작은 경우에만 분해합이 N이 가능함
        ans = 0
        n = i  # 현재 숫자 i 를 저장
        while i >= 1:
            ans += i%10  # 10으로 나눴을 때 나머지를 통해 각 자릿수를 더함
            i = i//10
        if n + ans == N:  # 생성자에 해당하는 경우만 리스트에 추가
            g_li.append(n)

    return g_li


N = int(input())

if len(generator(N)) == 0:
    print(0)
else:
    print(generator(N)[0])  # 생성자 리스트 중 가장 작은 값 출력