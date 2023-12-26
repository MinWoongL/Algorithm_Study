def solution(bandage, health, attacks):
    # answer = 0

    changed_health = health
    time = 0

    for a in attacks:
        if changed_health <= 0:
            return -1
        else:
            # 일단 주어진 health 이상 초과 no
            # 시전시간은 그동안 + 초당회복량이 된다는 소리
            # 시전시간동안 성공하면 + 추가회복량
            # 몬스터 공격받으면 시전시간 (cnt = 0)

            cnt = 0  # 연속 성공 횟수

            while time <= a[0]:  # 진행시간이 공격시간보다 작을경우
                cnt += 1
                if cnt < bandage[0]:  # 연속성공횟수가 시전횟수보다 작을 때
                    if health > changed_health + bandage[1]:
                        changed_health += bandage[1]
                    else:
                        changed_health = health
                    time += 1
                else:
                    cnt = 0
                    if health > changed_health + bandage[1] + bandage[2]:
                        changed_health += bandage[1] + bandage[2]
                    else:
                        changed_health = health
                    time += 1
            changed_health -= a[1]
            if changed_health <= 0:
                changed_health = -1
                break
            time += 1

    return changed_health

b = [5, 1, 5]
b2 = [3, 2, 7]

h = 30
h2 = 20

at = [[2, 10], [9, 15], [10, 5], [11, 5]]
at2 = [[1, 15], [5, 16], [8, 6]]

print(solution(b2, h2, at2))