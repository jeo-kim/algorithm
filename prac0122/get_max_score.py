def DFS(L, start, time, score):
    global max_score
    if time > max_time:
        if score-info[start-1][0] > max_score:
            max_score = score-info[start-1][0]
    elif time == max_time:
        if score > max_score:
            max_score = score
        return
    else:
        for i in range(start, n):
            DFS(L+1, i+1, time + info[i][1], score + info[i][0])

if __name__ == "__main__":

    n = 5
    max_time = 20
    info = [
        [10, 5],
        [25, 12],
        [15, 8],
        [6, 3],
        [7, 4]
    ]
    max_score = 0

    DFS(0, 0, 0, 0)

    print(max_score)