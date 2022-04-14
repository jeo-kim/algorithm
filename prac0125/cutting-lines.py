import sys

k,n = map(int, input().split())
lines = []

for _ in range(k):
    data = int(sys.stdin.readline().rstrip())
    lines.append(data)

lt = 1
rt = max(lines)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    pieces = 0
    for each_length in lines:
        pieces += each_length // mid

    if pieces >= n:
        res = mid
        lt = mid + 1

    elif pieces < n:
        rt = mid - 1


print(res)


