# 2630_색종이만들기_colored-paper
import sys
input = sys.stdin.readline

def cut_paper(board):
    global blue, white
    length = len(board)
    color = board[0][0]
    if length == 1:
        if color == 1:
            blue += 1
        else:
            white += 1
        return

    for i in range(length):
        check = True
        for j in range(length):
            if board[i][j] != color:
                check = False
                area1 = [[board[a][b] for a in range(length//2)] for b in range(length//2)]
                area2 = [[board[a][b] for a in range(length//2, length)] for b in range(length//2)]
                area3 = [[board[a][b] for a in range(length//2)] for b in range(length//2, length)]
                area4 = [[board[a][b] for a in range(length // 2, length)] for b in range(length // 2, length)]
                cut_paper(area1)
                cut_paper(area2)
                cut_paper(area3)
                cut_paper(area4)
                break
        if check is False:
            break
    else:
        if color == 1:
            blue += 1
        else:
            white += 1


N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0
cut_paper(paper)
print(white)
print(blue)
