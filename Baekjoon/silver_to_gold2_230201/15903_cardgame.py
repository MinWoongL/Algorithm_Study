# 15903_카드합체놀이_cardgame

n, m = map(int, input().split())

nli = list(map(int, input().split()))

for i in range(m):
    nli.sort()
    ans = nli[0] + nli[1]
    nli[0] = ans
    nli[1] = ans

print(sum(nli))

