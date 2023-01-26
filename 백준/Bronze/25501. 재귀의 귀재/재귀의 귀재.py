#  25501_재귀의 귀재_ isPalindrome
#  global 변수를 활용해서 함수 호출 count하기

def ispalindrome(word, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif word[l] != word[r]:
        return 0
    else:
        return ispalindrome(word, l+1, r-1)


N = int(input())

for i in range(N):
    s = input()
    ls = len(s)
    l, r = 0, ls-1
    count = 0

    print(ispalindrome(s, l, r), count)


