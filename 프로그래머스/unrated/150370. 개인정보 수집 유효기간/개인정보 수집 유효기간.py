def solution(today, terms, privacies):
    answer = []
    year, month, day = map(int, today.split('.'))

    t_di = {}
    for v in terms:
        s, n = v.split()
        t_di[s] = n

    for i in range(len(privacies)):
        y, m, d, s = privacies[i].replace(' ', '.').split('.')
        y = int(y)
        m = int(m)
        d = int(d)

        n = int(t_di[s])

        ny, nm, nd = y, m, d
        nm = n + m
        while nm > 12:
            nm -= 12
            ny += 1

        if nd == 1:
            nd = 28
            nm -= 1
        else:
            nd -= 1

        while True:
            if ny < year:
                answer.append(i+1)
                break

            if nm < month and ny == year:
                answer.append(i+1)
                break

            if nd < day and nm == month and ny == year:
                answer.append(i+1)
                break

            break

    return answer