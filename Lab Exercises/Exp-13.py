def minimax(depth, is_max):
    if depth == 3:
        return 0

    if is_max:
        best = -1000
        for score in [3, 5, 2]:
            best = max(best, score)
        return best
    else:
        best = 1000
        for score in [3, 5, 2]:
            best = min(best, score)
        return best

print("Best score:", minimax(0, True))
