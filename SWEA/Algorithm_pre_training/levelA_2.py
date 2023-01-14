#최대수 구하기
testcase = int(input())

for i in range(testcase):
    num = list(map(int,input().split()))
    max_num = max(num)
    print("#{} {}".format(i+1,max_num))