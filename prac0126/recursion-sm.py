import sys

import collections

sys.setrecursionlimit(10 ** 7)

nodes = int(sys.stdin.readline())
edges = collections.defaultdict(list)
parents = [-1] * 2 + [0] * (nodes - 1)

queue = collections.deque()

for _ in range(nodes - 1):
    edge = tuple(map(int, sys.stdin.readline().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])


def dfs(node):
    kids = edges[node]
    for kid in kids:
        if parents[kid] == 0:
            parents[kid] = node
            dfs(kid)
    return

dfs(1)

for i in parents[2:]:
    print(i)
