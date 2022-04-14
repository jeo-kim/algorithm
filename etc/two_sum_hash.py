from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hash_table = {}

    for idx, num in enumerate(nums):
        # 자신들의 정보를 저장한다.
        # hash_table[num] = idx  # 이게 여기 위치면 [2, 2]가 출력됨. (5, 5)
        if hash_table.get(target-num):
            return [hash_table.get(target-num), idx]
        hash_table[num] = idx  # 같은 수 중복ㅇ 아니라 서로 다른 수의 조합을 보려면 요기다.

print(twoSum([13,7,5,1,3,2], 10))