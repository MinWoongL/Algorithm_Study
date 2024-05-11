def solution(n, costs):
    
    def find(node):
        while parents[node] != node:
            node = parents[node]
        return node
    
    def union(x, y):
        parents[find(y)] = find(x)
        
        
    answer = 0
    
    parents = [i for i in range(n)]
    costs.sort(key=lambda x:x[2])
    
    cnt = 0
    for c in costs:
        s, e, v = c
        if find(s) != find(e):
            union(s, e)
            cnt += 1
            answer += v
            if cnt == n:
                break
    
    
    return answer