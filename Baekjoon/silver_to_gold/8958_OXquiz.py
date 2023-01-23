# 8958_OX 퀴즈

T = int(input())

for i in range(T):
    score = 0  # 총 점수
    streak = 0  # 연속으로 정답일 때 점수 누적
    text = str(input())
    for v in range(len(text)):
        if text[v] == "O":
            streak += 1
            score += streak
        else:
            streak = 0

    print(score)

