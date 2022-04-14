M = 11
jewels = [
    [5, 12],
    [3, 8],
    [6, 14],
    [4, 8]
]

dy = [0] * (M+1)

for i in range(len(jewels)):
    # 지금 따져보고 있는 보석의 무게(w)와 가치(v)
    w = jewels[i][0]
    v = jewels[i][1]
    # 자신의 무게에 해당하는 인덱스부터, 구하고자 하는 최대무게에 해당하는 인덱스까지
    # 쭉 돌면서 이전에 채워놓은 칸을 참고하여 가능한 최대 무게를 업데이트한다.
    for j in range(w, M+1):
        dy[j] = max(dy[j], dy[j-w] + v)

print(dy[M])