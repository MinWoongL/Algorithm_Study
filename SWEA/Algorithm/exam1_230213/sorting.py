def bubble_sort(li, N):
    for i in range(N-1,0,-1):
        for j in range(0, i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li


def counting_sort(A, B, k):

    C = [0]*(k+1)

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]


def selection_sort(li):
    for i in range(len(li)-1):
        idx = i
        for j in range(i + 1, len(li)):
            if li[idx] > li[j]:
                idx = j
        li[i], li[idx] = li[idx], li[i]

    return li

