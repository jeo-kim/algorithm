n = 7

dy = [0] * (n+1)
dy[1] = 1  # 직관적으로 알 수 있는 작은 단위에 대한 결론을 먼저 짓고.
dy[2] = 2

for i in range(3, n+1):
    dy[i] = dy[i-2] + dy[i-1]

print(dy[n])
