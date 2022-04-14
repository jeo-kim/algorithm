import collections
import heapq

cases = int(input())

for _ in range(cases):
    n, target_idx = map(int, input().split( ))
    # 문서 개수와, 찾고자 하는 문서의 인덱스를 받아온다.
    nums = list(map(int, input().split( )))

    isDuplicated = False

    for each_num in nums:
        if nums.count(each_num) > 1:
            isDuplicated = True
            break

    if isDuplicated:
        indexes = list(range(len(nums)))  # 지금 인덱스들 숫자 리스트도 만든다.

        count = 1  # pop 될때마다 세주기
        while True:
            if nums[0] == max(nums):  # 첫 번째 친구가 가장 우선순위가 크다면 pop.
                nums.pop(0)
                popped_i = indexes.pop(0)  # 인덱스를 받아온 리스트도 똑같이 움직여준다.

                if target_idx == popped_i:  # 혹시 방금 나간 인덱스가 타겟 인덱스라면
                    print(count)  # 타겟 문서가 지금 나갔다는 뜻이니까, 지금까지 pop 된 횟수를 출력해준다.
                    break

                count += 1

            else:  # 첫 번째 친구가 가장 큰 우선순위가 아니라면
                wasFirst = nums.pop(0)  # 앞에 있던 아이를 잠깐 빼서
                nums.append(wasFirst)  # 뒤로 이동.

                wasFirstIdx = indexes.pop(0)  # 인덱스 리스트에서도 똑같이 앞에꺼를 뒤로 이동..
                indexes.append(wasFirstIdx)

    else:  # 중복된 우선순위가 없는 경우라면 heap 을 사용해보면 어떨까.
        heap = []

        for idx, num in enumerate(nums):
            heapq.heappush(heap, (-num, num, idx))
            # 파이썬 내장 힙은 최소 힙만 지원한다고 함(우선순위(?) 최소값부터 제거할 수 있음)
            # 그걸 최대 힙으로 활용하려면 num 의 부호를 바꾸어서, 그걸 우선순위로 적용하면 됨. ( -num )
            # 인덱스를 기억해두어야 함..!

        count = 1
        while heap:
            a, b, c = heapq.heappop(heap)
            # 최대힙 정렬해둔 것에서 앞에꺼를 빼내는데, 언패킹해서 맨 뒤에 넣어놨던 인덱스 번호도 참조한다.
            if c == target_idx:  # 힙을 통해 지금 꺼낸 친구의 인덱스 번호가 타겟 인덱스라면
                print(count)  # 지금까지 pop 한 횟수를 출력.
                break
            count += 1