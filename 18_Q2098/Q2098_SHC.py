"""
외판원 순회
"""

from sys import setrecursionlimit, stdin

setrecursionlimit(1 << 30)

input = lambda: stdin.readline().strip()
INF = 1 << 30

N = int(input())
G = [[INF if x == "0" else int(x) for x in input().split()] for _ in range(N)]

# dp[cur][visit] = cur에서 visit(bitset)한 도시를 제외한 나머지를 방문하고 시작점으로 돌아오는 최소비용
dp = [[INF for _ in range((1 << N))] for _ in range(N)]


def dfs(x, visited: int) -> int:
    """
    - x: 현재 방문한 도시
    - visited: 지금까지 방문한 도시 (bitset)
    """
    if visited == (1 << N) - 1:
        # 모든 도시를 방문했다면
        return G[x][0]

    if dp[x][visited] != INF:
        return dp[x][visited]

    for i in range(N):
        if G[x][i] == INF or visited & (1 << i):
            continue
        dp[x][visited] = min(
            dp[x][visited], dfs(i, visited | (1 << i)) + G[x][i]  # x → i로 가는 경로를 DFS로 탐색
        )

    return dp[x][visited]


print(dfs(0, 1))
