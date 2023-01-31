# 2812_크게만들기_make-bigger

# 스택에 앞자리 수부터 최대한 큰 수만 저장

N, K = map(int, input().split())

number = list(input())
# print(number)

length_of_num = N-K
n_stack = [number[0]]

for i in range(1, N):
    while K > 0 and n_stack:  # K개 만큼 이미 제외했거나 스택이 비어있으면 append로 넘어가야 함.
        if n_stack[-1] < number[i]:
            n_stack.pop()
            K -= 1
        else:
            break
    n_stack.append(number[i])

# print(type(n_stack[0]))
# print(n_stack)
# print(*n_stack[0:length_of_num])
print(''.join(n_stack[0:length_of_num]))



