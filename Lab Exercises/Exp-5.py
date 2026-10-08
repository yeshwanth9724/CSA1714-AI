from collections import deque
start = (3, 3, 0)
goal = (0, 0, 1)
moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m and c > m:
        return False
    mr, cr = 3-m, 3-c
    if mr and cr > mr:
        return False
    return True
q = deque([(start, [])])
visited = {start}
while q:
    state, path = q.popleft()
    m, c, boat = state
    if state == goal:
        print("Solution:")
        for s in path + [state]:
            print(s)
        break
    for dm, dc in moves:
        if boat == 0:
            ns = (m-dm, c-dc, 1)
        else:
            ns = (m+dm, c+dc, 0)
        if valid(ns[0], ns[1]) and ns not in visited:
            visited.add(ns)
            q.append((ns, path + [state]))
