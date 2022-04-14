arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]

def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            # 엇 나보다 작은 값 발견했다면 앞쪽으로 보내줘야지
            # 저 앞에 pos 값하고 스왑해주자
            # 이제 pos 자리는 나(pivot)보다 작은 애로 잘 채웠으니까,
            # 다음에 작은애가 오면 그 다음칸에 채워줘야하니
            # pos 는 한 칸 앞으로 이동하자!
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)

Qsort(0, 9)
print(arr)