import sys
def tsp(graph, start):
    n = len(graph)
    dp = [[None] * (1 << n) for _ in range(n)]
    for i in range(n):
        if i != start:
            dp[i][1 << start | 1 << i] = graph[start][i]
    def solve(mask, pos):
        if dp[pos][mask] is not None:
            return dp[pos][mask]
        ans = sys.maxsize
        for next_pos in range(n):
            if next_pos != pos and mask & 1 << next_pos:
                new_mask = mask ^ (1 << next_pos)
                result = solve(new_mask, next_pos)
                if result is not None:
                    ans = min(ans, graph[pos][next_pos] + result)
        dp[pos][mask] = ans if ans != sys.maxsize else None
        return dp[pos][mask]
    return solve((1 << n) - 1, start)
if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start = 0
    print("Minimum cost:", tsp(graph, start))
