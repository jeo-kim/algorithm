arr = [23, 11, 45, 7, 15, 67, 33, 21]

def Dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2

        # 나의 왼/오 조각들이 먼저 정렬 처리를 해와야 하므로
        # 재귀적 호출을 먼저하고 완료되길 기다린다.
        Dsort(lt, mid)
        Dsort(mid+1, rt)

        # 왼/오 자식 조각들이 완료한 작업을 바탕으로
        # 이제 나의 레벨에서의 본연의 작업을 한다.
        p1 = lt
        p2 = mid+1
        tmp = []  # 내 레벨에서 정렬한 결과물을 담아두고, 이후 arr 에 복사하기 위한 리스트
        while p1 <= mid and p2 <= rt:  # p1이나 p2중 어느 하나가 자신의 구역을 다 훑으면 종료
            # 왼쪽에서 제일 작은애랑 오른쪽에서 제일 작은애가 비교해서, 그 중 더 작은애를 tmp 에 먼저 append.
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1  # tmp 에 붙였으니 포인터 한칸 전진

            else:
                tmp.append(arr[p2])
                p2 += 1

        if p1 <= mid:
            tmp = tmp + arr[p1:mid+1]
        if p2 <= rt:
            tmp = tmp + arr[p2:rt+1]
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]

Dsort(0, 7)
print(arr)
