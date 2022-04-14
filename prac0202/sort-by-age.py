import heapq
import sys

n = int(sys.stdin.readline().rstrip())
members = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    # 우선순위 1. 나이, 2. 가입순서(입력 받은 순서를 나타내는 i)
    heapq.heappush(members, (int(age), i, name))

for i in range(n):
    info = heapq.heappop(members)
    print(info[0], info[2])