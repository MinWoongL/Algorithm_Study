
score = []
for _ in range(5):
    tmp = int(input())
    if tmp <= 40:
        score.append(40)
    else:
        score.append(tmp)

print(sum(score)//5)