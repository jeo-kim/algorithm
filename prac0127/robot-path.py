def solution(dirs):
    x = 5
    y = 5
    path_set = set()

    for i in range(len(dirs)):
        tmp = (x, y)
        if dirs[i] == "U":
            if x-1 >= 0:
                path_set.add((tmp, (x-1, y)))
                path_set.add(((x-1, y), tmp))
                x -= 1
            else:
                continue
        elif dirs[i] == "D":
            if x+1 <= 10:
                path_set.add((tmp, (x+1, y)))
                path_set.add(((x+1, y), tmp))
                x += 1
            else:
                continue
        elif dirs[i] == "L":
            if y-1 >= 0:
                path_set.add((tmp, (x, y-1)))
                path_set.add(((x, y-1), tmp))
                y -= 1
            else:
                continue
        elif dirs[i] == "R":
            if y+1 <= 10:
                path_set.add((tmp, (x, y+1)))
                path_set.add(((x, y+1), tmp))
                y += 1
            else:
                continue
    answer = int(len(path_set) / 2)
    return answer
