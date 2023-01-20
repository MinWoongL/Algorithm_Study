Croa = {
    'c=': 1,
    'c-': 1,
    'dz=': 1,
    'd-': 1,
    'lj': 1,
    'nj': 1,
    's=': 1,
    'z=': 1,
}

word = str(input())
count = 0
for key in Croa:
    word = word.replace(key, '&')  # replace 함수는 copy를 제공하는함수, 원형을 바꿔줘야함. 아래 형태로는 바뀌질 않음
    #word.replace(key, '&')

print(len(word))