from collections import deque
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
q = deque([(start, [])])
visited = {start}
while q:
    state, path = q.popleft()
    if state == goal:
        print("Solution:", path)
        break
    z = state.index(0)
    r, c = divmod(z, 3)
    for dr, dc, move in [(1,0,"Down"), (-1,0,"Up"),
                         (0,1,"Right"), (0,-1,"Left")]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr * 3 + nc
            s = list(state)
            s[z], s[nz] = s[nz], s[z]
            s = tuple(s)
            if s not in visited:
                visited.add(s)
                q.append((s, path + [move]))
