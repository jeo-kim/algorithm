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
            DFS(L+1, i+info[i][0], pay + info[i][1])

if __name__ == "__main__":

    n = 7

    info = [
        [0, 0], # 이건 내가 추가..
        [4, 20],
        [2, 10],
        [3, 15],
        [3, 20],
        [2, 30],
        [2, 20],
        [1, 10]
    ]
    max_pay = 0

    DFS(0, 1, 0)

    print(max_pay)