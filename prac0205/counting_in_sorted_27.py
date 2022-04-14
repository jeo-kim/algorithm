import sys
import bisect

n, x = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# bisect_left 가 반환해주는 index 는 자기 왼쪽에는 다 target 보다 작다는 것을 의미
# bisect_right 는 나를 포함한 내 뒤에 있는 아이들은 다 target 보다 크다는 것을 의미
    # 그래서 left 는 target 이 처음 등장할 수 있는 인덱스로서 가능성이 있고
    # right 는 target 보다 직후에 있는 수로서 살펴볼 수 있다.

s = bisect.bisect_left(nums, x)
e = bisect.bisect_right(nums, x)

if s < len(nums) and nums[s] == x:
    print(e-s)
else:
    print(-1)




