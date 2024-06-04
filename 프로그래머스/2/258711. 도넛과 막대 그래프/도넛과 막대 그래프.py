from collections import deque
def solution(edges):
    adjL = [[] for _ in range(1000001)]
    in_info = {}
    out_info = {}
    main_node = -1
    for e in edges:
        if e[0] in in_info.keys():
            in_info[e[0]] += 1
        else:
            in_info[e[0]] = 1
        
        if main_node == -1 or in_info[e[0]] >= 2:
            if e[0] not in out_info.keys():
                main_node = e[0]
            
        if e[1] in out_info.keys():
            out_info[e[1]] -= 1
        else:
            out_info[e[1]] = -1
        
        adjL[e[0]].append(e[1])
    
    D, M, E = 0, 0, 0
    for n in adjL[main_node]:
        q = deque()
        is_cycle = False
        is_double = False
        is_self = False
        q.append(n)
        visited = set()
        visited.add(n)
        while q:
            now = q.popleft()
            
            if len(adjL[now]) > 1:
                is_double = True
                break
            for node in adjL[now]:
                if node == now:
                    D += 1
                    is_self = True
                    break
                if node not in visited:
                    visited.add(node)
                    q.append(node)
                else:
                    is_cycle = True
                    break
                    
        if not is_cycle and not is_double and not is_self:
            M += 1
            # print("M", n, M)
        if is_cycle and not is_double and not is_self:
            D += 1
            # print("D", n, D)
        if is_double:
            E += 1
            # print("E", n, E)
                    
    answer = [main_node, D, M, E]
    return answer