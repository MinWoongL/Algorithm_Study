# SWEA_병합정렬

def msort(li):  # 병합정렬
    # 종료조건으로 리스트 원소가 1개면 바로 반환
    global cnt
    if len(li) <= 1:
        return li
    mid = len(li) // 2
    left_li = li[:mid]
    right_li = li[mid:]

    # 숫자열의 반을 나눠 다시 병합정렬을 한 결과를 저장 (재귀)
    left_li = msort(left_li)
    right_li = msort(right_li)

    if left_li[-1] > right_li[-1]:
        cnt += 1

    # 정렬된 순서를 저장해줄 리스트 선언
    s_li = []
    i, j = 0, 0
    # 정렬된 left, right 숫자열들을 순서대로 비교하여 정렬
    while i < len(left_li) and j < len(right_li):
        if left_li[i] < right_li[j]:
            s_li.append(left_li[i])
            i += 1
        else:
            s_li.append(right_li[j])
            j += 1
    # 비교 후 아직 저장되지 않은 숫자들을 마저 정렬
    while i < len(left_li):
        s_li.append(left_li[i])
        i += 1
    while j < len(right_li):
        s_li.append(right_li[j])
        j += 1
    return s_li


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    ans = msort(lst)
    print(f'#{tc} {ans[N//2]} {cnt}')
