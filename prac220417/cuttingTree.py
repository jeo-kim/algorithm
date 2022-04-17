import sys

n, m = map(int, sys.stdin.readline().split()) # n은 나무 수, m은 필요한 길이
trees = list(map(int, sys.stdin.readline().split()))

lt = 0
rt = max(trees)
answer = 0

def howLongCanIGet(height):
    total = 0
    for tree in trees:
        length = 0
        if tree > height:
            length = tree - height
        total += length
    return total

while lt <= rt:
    mid = (lt + rt) // 2
    if howLongCanIGet(mid) >= m:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(answer)






