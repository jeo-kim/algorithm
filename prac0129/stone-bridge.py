# bottom-up
n = 7
dy = [0] * (n+2)
dy[1] = 1
dy[2] = 0

for i in range(3, n+2):
    if i == 5:
        dy[i] = 0
    else:
        dy[i] = dy[i-1] + dy[i-2]

print(dy[n+1])


# top-down
visited = [0]*(n+2)  # for memoization

def DFS(nth: int):
    if nth == 1:
        return 1
    if nth == 2:
        return 0
    if nth == 5:
        return 0
    else:
        if visited[nth] != 0:
            return visited[nth]
        else:
            visited[nth] = DFS(nth - 1) + DFS(nth - 2)
            return visited[nth]

print(DFS(n+1))