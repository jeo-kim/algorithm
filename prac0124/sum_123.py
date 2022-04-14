t = int(input())

def DFS(sum):
    global count
    global n
    if sum == n:
        count += 1
    elif sum > n:
        return
    else:
        for i in range(1, 4):
            DFS(sum + i)

for j in range(t):
    n = int(input())
    count = 0
    DFS(0)
    print(count)


