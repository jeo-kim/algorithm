n,c = map(int, input().split())
positions = []
for _ in range(n):
    pos = int(input())
    positions.append(pos)

lt = 1
rt = max(positions)
res = 0

def how_many_horses(distance):   # 최소 거리 distance 가 파라미터로 주어졌을 때 몇 마리까지 둘 수 있는지 알려주는 함수
    prev = 1  # 처음에 먼저 1번 위치에 말을 두고 시작하므로, 나보다 앞선 말의 위치(prev)의 초기값은 1
    count = 1  # 한 마리를 이미 두었으므로 count 초기값도 1
    for i in range(1, n):  # 인덱스 번호 1부터, 즉 두번째 마구간부터 검사 (여기에 말을 둘 수 있는지)
        if positions[i] - prev >= distance:  # distance 이상의 거리를 확보했다면
            count += 1  # 여기 말을 둘 것이므로 count + 1
            prev = positions[i]  # 다음 마구간 입장에서 말이 있는 가장 인접한 마구간은 여기가 될 것이므로 prev 업데이트

    return count

while lt <= rt:  # 왼쪽 끝점과 오른쪽 끝점이 같거나 교차하게 되면 탐색은 이미 종료된 것이므로 while 종료.
    mid = (lt + rt) // 2  # 매번 중간값 갱신
    cnt = how_many_horses(mid)
    if cnt >= c:  # mid 를 최소거리로 삼을 경우 c 마리 이상 놓을 수 있다면 조건에 부합하는 것이므로 우선 res 에 업데이트해두고, 더 긴 거리도 가능한지 알아보기 위해 lt를 mid 오른쪽으로 옮김
        res = mid
        lt = mid+1
    else:  # 지금 mid로는 c마리 보다 적게 놓인다면 최소거리를 줄여야 하므로 rt를 mid-1로 옮겨 작은 범위에서 탐색
        rt = mid-1

print(res)
