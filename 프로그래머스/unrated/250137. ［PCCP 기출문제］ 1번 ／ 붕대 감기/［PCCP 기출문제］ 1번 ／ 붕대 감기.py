import sys
input = sys.stdin.readline

def solution(bandage, health, attacks):
    answer = 0
    t = 0
    c_time, hp_reco, bonus_reco = bandage
    now_h = health
    for at in attacks:
        h_time, damage = at
        if (h_time - t - 1) >= c_time:
            bonus = bonus_reco*((h_time-t)//c_time)
            reco = hp_reco*(h_time-t)
            total_reco = bonus+reco
        else:
            total_reco = hp_reco*(h_time - t - 1)

        now_h += total_reco

        if now_h > health:
            now_h = health

        now_h -= damage

        if now_h <= 0:
            return -1

        answer = now_h
        t = h_time

    return answer