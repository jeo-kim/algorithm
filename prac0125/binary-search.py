sorted_list = [1, 4, 7, 10, 12, 26, 35, 41, 46, 50, 78, 83, 97]

lt = 0
rt = len(sorted_list)-1
target = 26

while lt<=rt:
    mid = (lt+rt)//2
    if sorted_list[mid] > target:
        rt = mid - 1
    elif sorted_list[mid] < target:
        lt = mid + 1
    else:  # mid 인덱스에 위치한 것이 내가 딱 원하던 타겟 숫자라면
        print(f"{mid + 1}번째 위치에 26이 있어요. : {sorted_list[mid]}" )
        break
