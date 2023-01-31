# 10814_나이순정렬_age-sorting

n = int(input())

age_li = []

for i in range(n):
    #  입력값을 받을 때, 변수 타입에 주의해야함. str로 받으면 오름차순 정렬시 10, 9로 정렬되서 오답
    age_name = list(map(str, input().split()))
    age_name.append(i)
    age_li.append([int(age_name[0]),age_name[1],age_name[2]])

# print(age_li)

# 다중 key를 사용하여 정렬 시, tuple 형식으로 순서를 부여해준다 (내림차순은 - 붙여준다)

age_li = sorted(age_li, key=lambda x: (x[0], x[2]))
# print(age_li)

ans_li = []
for v in age_li:
    ans_li.append([str(v[0]), v[1]])

for value in ans_li:
    print(' '.join(value))
