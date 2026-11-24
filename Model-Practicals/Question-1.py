from collections import deque
def bfs(g, s, goal):
    q1, q2 = deque([[s]]), deque([[goal]])
    v1, v2 = {s: [s]}, {goal: [goal]}
    while q1 and q2:
        p = q1.popleft()
        for x in g[p[-1]]:
            if x in v2:
                return p + v2[x][-2::-1]
            if x not in v1:
                v1[x] = p + [x]
                q1.append(v1[x])
        p = q2.popleft()
        for x in g[p[-1]]:
            if x in v1:
                return v1[x] + p[-2::-1]
            if x not in v2:
                v2[x] = p + [x]
                q2.append(v2[x])
    return "No path found"
g = {'A':['B','C'], 'B':['A','D'],
     'C':['A','E'], 'D':['B','F'],
     'E':['C','F'], 'F':['D','E']}
print("Path:", bfs(g, 'A', 'F'))
