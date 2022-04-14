import bisect


def binary_search(arr, target, start, end, L):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return mid, L
    else:
        if arr[mid] < target:
            return binary_search(arr, target, mid+1, end, L+1)
        else:
            return binary_search(arr, target, start, mid-1, L+1)

arr1 = ["apple", "banana", "cherry", "orange"]

result = binary_search(arr1, "apple", 0, len(arr1)-1, 1)

if result is None:
    print("Target doesn't exist.")
else:
    print(f"Target exists at idx {result[0]}. We found it in {result[1]} times")


bisect.bisect_left()