import sys

cases = int(input())

for _ in range(cases):  # 케이스 횟수
    n,target_idx = map(int, sys.stdin.readline().split( ))  # 랑, 타겟 인덱스
    nums = list(map(int, input().split()))
    indexes = list(range(len(nums)))  # 지금 인덱스들 숫자 리스트도 만든다.

    count = 1  # pop 될때마다 세주기

    while True:
        if nums[0] == max(nums):  # 첫 번째 친구가 가장 우선순위가 크다면 pop.
            nums.pop(0)
            # indexes.pop(0)  # 인덱스를 받아온 리스트도 똑같이 움직여준다.
            popped_i = indexes.pop(0)

            # if target_idx not in indexes:  # 혹시 방금 최댓값 나가면서 타겟 인덱스도 나갔다면
            if target_idx == popped_i:  # 혹시 방금 나간 인덱스가 타겟 인덱스라면
                print(count)  # 타겟 문서가 지금 나갔다는 뜻이니까, 지금까지 pop 된 횟수를 출력해준다.
                break

            count += 1

        else:
           wasFirst = nums.pop(0)
           nums.append(wasFirst)

           wasFirstIdx = indexes.pop(0)
           indexes.append(wasFirstIdx)




