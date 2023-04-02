pat = {
    (2,1,1):0,
    (2,2,1):1,
    (1,2,2):2,
    (4,1,1):3,
    (1,3,2):4,
    (2,3,1):5,
    (1,1,4):6,
    (3,1,2):7,
    (2,1,3):8,
    (1,1,2):9
}
for tc in range(int(input())):
    n, m = map(int, input().split())
    li = list(set([input() for _ in range(n)]))
    ans = 0
    tmp = []
    for i in li:
        res = format(int(i, 16), 'b').lstrip('0')
        a, b, c = 0, 0, 0
        cnt = 0
        x, y = 0, 0
        over = ''
        for j in res:
            if j == '1' and b == 0:
                a += 1
            elif j == '0' and a != 0 and c == 0:
                b += 1
            elif j == '1' and b != 0:
                c += 1
            elif c != 0:
                cnt += 1
                k = min(a, b, c)
                nums = pat[(a//k, b//k, c//k)]
                over += str(nums)
                if cnt == 8:
                    if (x * 3 + y + nums) % 10 == 0 and over not in tmp:
                        ans += x+y+nums
                    tmp.append(over)
                    x, y, cnt = 0, 0, 0
                    over = ''
                elif cnt % 2 == 0:
                    y += nums
                else:
                    x += nums
                a, b, c = 0, 0, 0
    print(f'#{tc+1} {ans}')

'''
# 교수님 풀이
pat = {211:0,
       221:1,
       122:2,
       411:3,
       132:4,
       231:5,
       114:6,
       312:7,
       213:8,
       112:9}
 
def erase(i, j, x, N):
    while i<N and bit[i][j-1]:
        for c in range(j-1-(56*x-1),j):
            bit[i][c] = 0
        i += 1
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    scan = [input() for _ in range(N)]
    bit = [[0]*(M*4) for _ in range(N)]
    # 16진수 -> 2진수 패턴 변환
    for i in range(N):
        for j in range(M):
            dec = int(scan[i][j], 16)
            for k in range(3, -1, -1):
                bit[i][j*4+3-k] = 1 if dec&(1<<k) else 0
        # print(bit[i])     # 1단계
    # 0101 반복구간 찾기
    M *= 4
    ans = 0
    for i in range(N):
        j = 0
        pwd = [0] * 8
        pwdcnt = 0
        while j<M:
            cnt = [0] * 3
            while j<M and bit[i][j] == 0: # 1이 나올 때 까지 이동
                j += 1
            while j<M and bit[i][j] == 1: # 1의 개수
                cnt[0] += 1
                j += 1
            while j<M and bit[i][j] == 0: # 0의 개수
                cnt[1] += 1
                j += 1
            while j<M and bit[i][j] == 1: # 1의 개수
                cnt[2] += 1
                j += 1
            ratio = min(cnt)
            if ratio:       # 0이 아니면
                pwd[pwdcnt] = pat[cnt[0]//ratio*100 + cnt[1]//ratio*10 + cnt[2]//ratio]
                pwdcnt += 1
                if pwdcnt == 8:
                    if (sum(pwd[0:8:2])*3 +sum(pwd[1:8:2]))%10==0:
                        ans += sum(pwd)
                    erase(i, j, ratio, N)
                    pwdcnt = 0
    print(f'#{tc} {ans}')
'''