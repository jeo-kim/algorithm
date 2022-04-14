n = int(input())
info = [(0,0)]
for _ in range(n):
    t, p = map(int, input().split())
    info.append((t, p))
max_pay = 0
def DFS(L, start, pay):
    global max_pay
    global info
    global n
    if start >= n+1:
        if pay > max_pay:
            max_pay = pay
        return

    else:
        for i in range(start, n+1):
            if info[i][0] + i > n:
                continue
            DFS(L+1, i+info[i][0], pay + info[i][1])

DFS(0,1,0)
print(max_pay)
