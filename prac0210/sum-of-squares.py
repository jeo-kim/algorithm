import sys

n = int(sys.stdin.readline().rstrip())

# 초기화에 사용하는 큰 수
INF = int(1e6)

# 동적으로 기입해갈 배열 준비
dy = [INF] * (n+1)
dy[0] = 0

# 사용할 제곱수 종류들을 원소로 갖는 리스트 만들기
squares = []
root = 1
while root*root <= n:
    squares.append(root*root)
    root += 1

# 큰 수부터 검토하면 갱신 횟수 줄지 않을까 싶어서.. 그런데 sort 가 더 비용이 드나..?
squares.sort(reverse=True)

for k in squares:
    for i in range(k, n+1):
        dy[i] = min(dy[i], dy[i-k]+1)

print(dy[n])



