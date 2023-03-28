T = int(input())


# cnt : 교환 진행 횟수
def perm(cnt):
    global answer
    # 종료 조건??? idx 는 사용 불가능
    # 교환 횟수를 다 사용 했다면 ?? 최대 상금 구하기
    if cnt == change:
        answer = max(answer, int("".join(num)))
        return

    # 재귀 호출
    # 교환횟수가 남았다면 카드 바꿔준다.
    # 이 문제에서는 동일위치 교환 허용
    # 교환할 위치 2개를 교환할 때마다 새로 정해 주어야 한다.
    # 앞 위치 = i, 뒤 위치 j
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            # 자리 바꿔 보기
            num[i], num[j] = num[j], num[i]
            # 자리를 바꾼 상태로 다음 자리 바꾸러 가보기
            perm(cnt + 1)
            # 원상복구
            num[i], num[j] = num[j], num[i]


for tc in range(1, T + 1):
    num, change = input().split()
    num = list(num)  # 초기 숫자 판
    change = int(change)  # 교환 횟수

    # 순열을 구할때 경우의 수는 자리를 바꿀때 문자열의 길이만큼만 바꾸면 모든 경우의 수를 다 구할수 있어
    # 교환 횟수가 문자열의 길이보다 클때 굳이 더 진행 할 필요가 없겠다.
    # 문자열의 길이만큼 교환을 진행하고 남은 교환횟수 ( 주어진 교환 횟수와의 차이)가 홀수 or 짝수
    if change > len(num):
        # 남은 횟수가 홀수
        if (change - len(num)) % 2 == 1:
            change = len(num) - 1
        # 남은 횟수가 짝수
        else:
            change = len(num)

    # 최대 상금
    answer = 0
    # 교환 횟수는 0부터 시작
    perm(0)
    print(f"#{tc} {answer}")
