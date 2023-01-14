# 평균값구하기
import sys

testcase = int(input())

for i in range(testcase):
    num = list(map(int,input().split()))
    avg_num = sum(num)/len(num)
    avg_num = round(avg_num)
    print("#{} {}".format(i+1,avg_num))

# num = list(map(int,input().split()))
# avg_num = sum(num)/len(num)
# avg_num = round(avg_num)
#
# print(avg_num)

