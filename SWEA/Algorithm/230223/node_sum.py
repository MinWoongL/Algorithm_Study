# 노드의 합_서울2반_이민웅

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    heap = [0]*(N+2)    # 가장 끝에 노드는 j*2+1 이 존재 하지 않을수도 있음으로 N+2만큼 크기로 생성
    last = 0
    for _ in range(M):
        node_num, value = map(int, input().split())
        heap[node_num] = value

    for j in range(N-M, 0, -1):
        heap[j] = heap[j*2] + heap[j*2+1]

    print(f'#{tc} {heap[L]}')

