def alphabeta(depth, node, maximizing, values, alpha, beta):
    if depth == 3:
        return values[node]

    if maximizing:
        best = -float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

print("Alpha-Beta Pruning Algorithm")
result = alphabeta(0, 0, True, values,
                   -float('inf'), float('inf'))
print("Leaf Values:", values)
print("Optimal Value:", result)
