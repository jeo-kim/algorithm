import sys
# 준비
# 집의 수와 공유기 개수 받아오기
n, c = map(int, sys.stdin.readline().split())
# 집들의 x 좌표값 받기
locations = []
for _ in range(n):
    location = int(sys.stdin.readline())
    locations.append(location)
# 집의 좌표 오름차순 정렬
locations.sort()

# 가장 인접한 공유기 간의 거리가 주어졌을 때 몇 개의 집까지 설치할 수 있는지 세 주는 함수
def how_many(min_dis):
    recent = locations[0]
    count = 1
    for i in range(1, n):
        cur = locations[i]
        dis = cur - recent
        if dis < min_dis:
            continue
        else:
            count += 1
            recent = cur
    return count

# 가장 인접한 공유기 간의 거리가 나올 수 있는 값의 범위를 정해두고,
# 계속해서 mid 를 조정(이분탐색)해가면서 조건을 충족하는 mid 를 찾기
start = 1
end = locations[-1]
answer = 0

while start <= end:
    mid = (start+end)//2
    # 설치해야 하는 공유기 수와 같거나 더 많이 설치할 수 있다면, 정답후보로 반영, 더 큰 값의 범위에서 거리(mid) 탐색
    if how_many(mid) >= c:
        answer = max(answer, mid)
        start = mid +1
    # 설치해야 하는 공유기 수만큼 설치할 수 없으면, 더 작은 값의 범위에서 거리(mid) 탐색
    else:
        end = mid - 1

print(answer)

