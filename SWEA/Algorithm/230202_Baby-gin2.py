# Baby-gin Game

# 0~9 사이 임의의카드 6장, 연속적인 세 개의 번호 = run, 동일한 세 개의 번호 = triplet

N = list(map(int,input()))

print(N)


def p_li(li):
    ans_li = []
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            for k in range(j+1,len(li)):
                if [li[i],li[j],li[k]] not in ans_li:
                    idx_li = [i for i in range(len(li))]
                    idx_li.remove(i)
                    idx_li.remove(j)
                    idx_li.remove(k)
                    ans_li.append([li[i],li[j],li[k],[li[idx_li[0]], li[idx_li[1]], li[idx_li[2]]]])
    return ans_li


new_li = p_li(N)

for v in new_li:
    if (abs(v[0] - v[1]) == 1 and abs(v[1] - v[2])) == 1 or (abs(v[1] - v[2]) == 1 and abs(v[2]-v[0] == 1)):
        if v[3][0]+v[3][1]+v[3][2] / 3 == v[3][0]:
            print('baby-gin')
            break
        elif abs((v[3][0]-v[3][1]) == 1 and abs(v[3][1]-v[3][2])) or (abs(v[3][1]-v[3][2]) and abs(v[3][2]-v[3][0])):
            print('baby-gin')
            break
        else:
            print('baby-gin 아님!!')
            break
    elif v[0] == v[1] and v[1] == v[2]:
        if v[3][0] == v[3][1] and v[3][1] == v[3][2]:
            print('baby-gin')
            break
        elif abs((v[3][0]-v[3][1]) == 1 and abs(v[3][1]-v[3][2])) or (abs(v[3][1]-v[3][2]) and abs(v[3][2]-v[3][0])):
            print('baby-gin')
            break
        else:
            print('baby-gin 아님!!')
            break



