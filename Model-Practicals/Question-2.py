import heapq
goal = (1,2,3,4,5,6,7,8,0)
def h(s):
    return sum(s[i] != goal[i] and s[i] != 0
               for i in range(9))
def best(s):
    q = [(h(s), s)]
    seen = set()
    while q:
        _, s = heapq.heappop(q)
        if s in seen:
            continue
        seen.add(s)
        print(s[:3], s[3:6], s[6:])
        if s == goal:
            print("Goal Reached")
            return
        z = s.index(0)
        for n in [z-3, z+3, z-1, z+1]:
            if 0 <= n < 9 and not (abs(n-z)==1 and n//3 != z//3):
                t = list(s)
                t[z], t[n] = t[n], t[z]
                t = tuple(t)
                if t not in seen:
                    heapq.heappush(q, (h(t), t))

s = (1,2,3,4,0,6,7,5,8)
best(s)
