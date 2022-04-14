n = 9
k = 9
musics = [1,2,3,4,5,6,7,8,9]
cp_musics = musics[:]

lt = max(musics)
rt = sum(musics)

# how_many 나의 코드
def how_many_1(mid):
    total = 0
    count = 0
    for i in range(n-1):
        total += musics[i]
        if total + musics[i+1] > mid:
            count += 1
            total = 0
    return count + 1

# how_many 강사님 코드에서 배운 점들
# (1) for 문 작성 방식: 나는 한 번의 for 문에서 i 와 i +1 을 둘 다 다루고 있었던 것에 비해 강사님은 i 번째만을 다룬다.
# (2) 변수 초기화 방식: cnt 를 1로 초기화함으로써 나중에 cnt +1 을 하지 않고 리턴할 수 있다는 점이 훨씬 직관적이다.
# (3) 파라미터 명명방식: 외부에서 사용될 mid 라는 변수명은 중요하지 않으므로, 오히려 함수에서의 의미에 맞게 인자를 명명하는 것이 좋을 것이다.
def how_many_2(capacity):
    cnt = 1
    sum = 0
    for x in musics:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if how_many_1(mid) <= k:
        res = mid
        rt = mid - 1
    elif how_many_1(mid) >= k:
        lt = mid + 1

print(res)
