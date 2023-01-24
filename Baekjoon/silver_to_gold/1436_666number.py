# 1436_영화감독 숌

# 666이 포함된 N번째 작은 숫자 -> 5666 다음은 6666 이 아니라 6660임

n = int(input())
count = 0
num = 666
while count != n:
    if '666' in str(num):
        count += 1
    num += 1
print(count, num-1)