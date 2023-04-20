l_di = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6
}
def solution(lottos, win_nums):
    cnt = 0
    num_of_zeros = 0
    for v in lottos:
        if v in win_nums:
            cnt += 1
        elif v == 0:
            num_of_zeros += 1

    answer = []
    answer.append(l_di[cnt])
    answer.append(l_di[cnt+num_of_zeros])
    answer.sort()

    return answer