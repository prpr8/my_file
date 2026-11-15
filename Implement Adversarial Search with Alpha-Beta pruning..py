import math

values = [3, 5, 6, 9, 1, 2, 0, -1]

def alphabeta(depth, nodeIndex, maxPlayer, values, alpha, beta):
    # Base case: reached a leaf node
    if depth == 3:
        return values[nodeIndex]

    if maxPlayer:
        best = -math.inf                      # FIXED: was math.inf
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print("Pruning at MAX node")
                break

        return best

    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)            # FIXED: use best (consistent with MAX)

            if beta <= alpha:
                print("Pruning at MIN node")
                break

        return best


print("Leaf Node values :", values)

result = alphabeta(
    depth=0,
    nodeIndex=0,
    maxPlayer=True,
    values=values,
    alpha=-math.inf,                          # FIXED: was math.inf
    beta=math.inf
)

print("Optimal Value :", result)
