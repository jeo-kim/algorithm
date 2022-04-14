import sys

n = int(sys.stdin.readline().rstrip())

# 초기화에 사용할 큰 수
INF = int(1e5)

# 동적으로 기입할 배열
dy = [INF] * (n+1)
dy[3] = 1

# 3kg 봉지만 고려하는 경우
for i in range(4, n+1):
    dy[i] = min(dy[i], dy[i-3] + 1)

# 5kg 봉지도 고려하는 경우
if n >= 5:
    dy[5] = 1
    for j in range(6, n+1):
        dy[j] = min(dy[j], dy[j-5] + 1)

# 3과 5로 딱 떨어지게 담을 수 없는 경우 INF 로 남아있음 => -1 리턴
if dy[n] == INF:
    print(-1)
else:
    print(dy[n])
