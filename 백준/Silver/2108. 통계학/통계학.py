import sys
import operator


def arithmetic(li):
    return round(sum(li)/len(li))


def median(li):
    li.sort()
    return li[len(li)//2]


def mode(li):
    if len(li) == 1:
        return li[0]
    else:
        ndi = {}
        for v in li:
            if v not in ndi.keys():
                ndi[v] = 1
            else:
                ndi[v] += 1
        # print(ndi)
        ndi = sorted(ndi.items(), key=operator.itemgetter(1))
        # print(ndi)
        # print(len(ndi))
        idx = -1
        if ndi[idx][1] == ndi[idx - 1][1]:
            while ndi[idx][1] == ndi[idx - 1][1] and abs(idx) != (len(ndi) - 1):
                idx -= 1
            if abs(idx) == (len(ndi) - 1) and ndi[idx][1] == ndi[idx-1][1]:
                return ndi[idx][0]
            else:
                return ndi[idx+1][0]
        else:
            return ndi[idx][0]


def num_range(li):
    ma_value = max(li)
    mi_value = min(li)

    return ma_value - mi_value


N = int(input())

nli = [int(sys.stdin.readline().strip()) for _ in range(N)]
# print(nli)

print(arithmetic(nli))
print(median(nli))
print(mode(nli))
print(num_range(nli))