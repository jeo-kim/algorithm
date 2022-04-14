def solution(sizes):
    max_left = 0
    max_right = 0

    for pair in sizes:
        if pair[0] > pair[1]:
            pair[0], pair[1] = pair[1], pair[0]

        if pair[0] > max_left:
            max_left = pair[0]

        if pair[1] > max_right:
            max_right = pair[1]

    return max_left * max_right

sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
solution(sizes1)
solution(sizes2)
solution(sizes3)
