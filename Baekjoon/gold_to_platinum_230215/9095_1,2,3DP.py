# 9095_1,2,3더하기_1,2,3-DP

T = int(input())

test_li = [int(input()) for _ in range(T)]
# print(test_li)

for N in test_li:
    dp = [set()]*(N+1)
    if N == 1:
        print(1)
    elif N == 2:
        print(2)
    elif N == 3:
        print(4)
    else:
        dp[1] = {'1'}
        dp[2] = {'11', '2'}
        dp[3] = {'111', '12', '21', '3'}

        for i in range(4, N+1):
            dp_set = set()
            for s in range(1, 4):
                ss = str(s)
                for value in dp[i-s]:
                    dp_set.add(ss+value)
                    dp_set.add(value+ss)
            dp[i] = dp_set
        # print(dp)
        print(len(dp[N]))
