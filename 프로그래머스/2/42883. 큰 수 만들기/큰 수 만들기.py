
def solution(number, k):
    stack = []
    idx = 0
    l = len(number)
    while idx < l:
        if not k:
            break
        if not stack:
            stack.append(number[idx])
        else:
            while stack and stack[-1] < number[idx] and k:
                stack.pop()
                k -= 1
            stack.append(number[idx])
        idx += 1
    if not k:
        answer = ''.join(stack) + number[idx:]
    else:
        answer = number[:l-k]
        
    return answer