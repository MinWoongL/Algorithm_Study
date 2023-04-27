import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
good = 0
for a in range(N):
    target = num[a]
    left, right = 0, N-1

    while left < right:
        # 타겟일 때
        if num[left] + num[right] == target:
            if left != a and right != a:
                good += 1
                break
            elif left == a:
                left += 1
            else:
                right -= 1
        # 타겟보다 작을 때
        elif num[left] + num[right] < target:
            left += 1
        # 타겟보다 클 때
        else:
            right -= 1


print(good)