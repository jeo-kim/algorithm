# n = 5
import sys
n = int(input())
coordinate = [
    list(map(int, sys.stdin.readline().split())) for _ in range(n)
]

# 하위 우선순위기준부터
coordinate.sort(key=lambda x: x[1])

# 상위 우선순위기준을 가장 마지막에 적용
coordinate.sort(key=lambda x: x[0])

for i in range(n):
    print(coordinate[i][0], coordinate[i][1])
