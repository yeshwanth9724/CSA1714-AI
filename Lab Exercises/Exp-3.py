from collections import deque
A, B, target = 4, 3, 2
q = deque([((0, 0), [])])
visited = {(0, 0)}
while q:
    (a, b), path = q.popleft()
    if a == target or b == target:
        print("Solution:")
        for x in path:
            print(x)
        print((a, b))
        break
    states = [
        ((A, b), "Fill A"),
        ((a, B), "Fill B"),
        ((0, b), "Empty A"),
        ((a, 0), "Empty B"),
        ((a - min(a, B-b), b + min(a, B-b)), "A -> B"),
        ((a + min(b, A-a), b - min(b, A-a)), "B -> A")
    ]
    for s, move in states:
        if s not in visited:
            visited.add(s)
            q.append((s, path + [move]))
