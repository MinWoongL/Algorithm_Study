tn = int(input())
count = 0
for i in range(tn):
    li = []
    checker = True
    text = str(input())
    for j in range(1,len(text)):
        if text[j] == text[j-1]:
            pass
        else:
            if text[j-1] not in li:
                li.append(text[j-1])
            else:
                checker = False
                
    if text[-1] in li:
        checker = False
        
    if checker == True:
        count += 1

print(count) 