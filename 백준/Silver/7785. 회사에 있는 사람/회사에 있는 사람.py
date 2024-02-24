import sys
input = sys.stdin.readline

N = int(input())

employee = {}
emp_lst = []
for _ in range(N):
    name, info = input().split()

    if name in employee.keys():
        if info == 'enter':
            employee[name] = 1
        else:
            employee[name] = 0
    else:
        employee[name] = 1
        emp_lst.append(name)

emp_lst.sort(reverse=True)

for v in emp_lst:
    if employee[v]:
        print(v)

