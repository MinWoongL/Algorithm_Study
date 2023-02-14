# 1874_스택수열
n = int(input())

nli = [i for i in range(1, n+1)]
stack = []
pp_li = []
max_value = 0
for i in range(n):
    num = int(input())
    if not stack:
        for j in range(max_value, num):
            stack.append(nli[j])
            pp_li.append('+')

        stack.pop()
        pp_li.append('-')
        max_value = num

    else:
        if stack[-1] == num:
            stack.pop()
            pp_li.append('-')
        else:
            if num < stack[-1]:
                print('NO')
                pp_li.clear()
                break
            else:
                for k in range(max_value, num):
                    stack.append(nli[k])
                    pp_li.append('+')

                stack.pop()
                pp_li.append('-')
                max_value = num

if pp_li:
    for v in pp_li:
        print(v)

