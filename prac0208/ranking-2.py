results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
n = 5


def solution(n, results):

    INF = int(1e9)
    compare = [[INF]*(n+1) for _ in range(n+1)]

    for result in results:
        compare[result[0]][result[1]] = 1

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                compare[a][b] = min(compare[a][b], compare[a][k]+compare[k][b])

    ans = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if compare[i][j] != INF or compare[j][i] != INF:
                cnt += 1
        if cnt == n-1:
            ans += 1

    return ans

solution(n, results)