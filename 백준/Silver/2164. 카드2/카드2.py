from collections import deque

T = int(input())

deque = deque([i for i in range(1, T+1)])

while (len(deque) > 1):
    deque.popleft()
    tmp = deque.popleft()
    deque.append(tmp)
    
print(deque[0])
