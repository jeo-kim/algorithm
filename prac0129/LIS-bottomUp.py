arr = [5,3,7,8,6,2,9,4]

# 각 인덱스의 값이 증가수열의 마지막 값일 경우에 취할 수 있는 최장 증가수열의 길이를 적어두는 곳
max_len_when_this_is_last = [0] * len(arr)

# 바로 알 수 있는 작은 단위의 답부터 결정짓기
max_len_when_this_is_last[0] = 1
max_len_when_this_is_last[1] = 1
# 3번째부터는 앞선 인덱스에 있는 arr 의 값들 중 자신보다 작은 경우에,
# 그 친구들이 이미 만들어 놓은 최대 길이 수들을 돌아가면서 가장 큰 것으로 갱신한다.
# 만약 앞선 값 중 자기보다 작은 값이 없더라도 초기화해둔 0은 의미있게 쓰이는데,
# 나중에 +1하면 자기 자신만을 길이로 취하는 경우가 되기 때문

for i in range(2, len(arr)):
    max_len = 0
    for j in range(0, i):
        if arr[j] < arr[i]:
            max_len = max(max_len, max_len_when_this_is_last[j])

    max_len_when_this_is_last[i] = max_len + 1

print(max(max_len_when_this_is_last))