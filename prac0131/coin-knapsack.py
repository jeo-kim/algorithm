import sys

n, target_amount = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

# 최소값으로 업데이트되어야 하므로, 첫 수는 아주 크게
# 가능한 최대 금액(10,000) / 최소 동전 금액(1) 한 것보다 1 크게 초기화.
dy = [10001] * (target_amount + 1)

# 확실하게 알 수 있는 부분 확정(0원에 대한 답은 0개의 동전)
dy[0] = 0

for i in range(len(coins)):
    # 각 동전마다의 점진적으로 하는 기록은, 자신의 액수번째 j 부터 target_amount 가 되는 j까지.
    for j in range(coins[i], target_amount+1):
        # j 액수에 대해 i번째 동전을 반영한 최소 개수를 구해보고(dy[j-coins[i]] + 1)
        # 기존 값보다 더 작으면 업데이트
        dy[j] = min(dy[j], dy[j-coins[i]] + 1)

# 한번도 주어진 동전들에 의해 딱 채워진 적이 없는 경우에 해당
if dy[target_amount] >= 10001:
    print(-1)
# 답 제출
else:
    print(dy[target_amount])



