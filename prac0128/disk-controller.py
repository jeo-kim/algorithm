
# 말로 계획 먼저 해보기
# 이전 작업의 종료시점을 정한다.
# 그 종료시점보다 작거나 같은 요청시간을 가진 작업들을 불러온다.
# 그 작업들을, 소요시간(job[1])을 기준으로 우선순위큐에 넣는다.

# 소요시간이 작은 것 부터 get 해서
# 작업 상황을 업데이트 하는데 => 이 때 할 일들에는
# 1) 이전 작업의 종료시점에다가, 현재 큐에서 get 된 친구의 소요시간 job[1] 을 더해주어 -> 그 다음에 참고할 '이전작업 종료시점(prev)'을 갱신해준다.
# 2) 지금 추가한 작업은 요청시점부터 완료시점까지 총 얼마나 걸렸는지를 구해야 하는데 -
#   2-1) 업데이트한 prev(지금까지의 작업 종료시점) 에서 방금 get 한 친구의 요청시점(job[0])을 빼준다.
#       --> 이것을 따로 '총 대기시간?sum?' 에 += 해준다.
#        --> 그리고 get 해서 하나씩 작업을 확정할 때마다 count += 1 해준다. (언제 이 반복을 끝낼지 알기 위해서)

# get 하나를 해서 prev 가 재설정되었으므로
# 다시 이 종료시점보다 작거나 같은 요청시간을 가진 작업들을 불러온다.
# 그 작업들을, 소요시간(job[1])을 기준으로 우선순위 큐에 넣는다. ... 반복

# 반복은 언제까지 하는가? count == len(jobs) 가 될때까지. 즉 while count < len(jobs):
# (아니면.. jobs 추가할 때마다, jobs 리스트에서 하나씩 remove 해서 len(jobs) == 0 이 되는 시점에 종료 할 수도)

import heapq

def solution(jobs):
    num_of_jobs = len(jobs)
    # 이전 작업 종료시점
    prev_t = 0
    # 최소값을 우선 뽑기 위한 heap 리스트 준비
    heap = []
    # 총 대기시간 더해갈 변수 준비
    wait_sum = 0

    while len(jobs) > 0:
        # 만약 현재 작업 종료시점에서 시작될 수 있는 작업이 없다면 checked = False 라는 신호를 줘서, 그냥 시간+=1 하고 다시 while 문 돌 수 있게 하기
        checked = False
        heap.clear()
        # prev 보다 요청시간 작거나 같아서 후보될 수 있는 아이들 넣을 것.
        for i, job in enumerate(jobs):
            if job[0] <= prev_t:
                heapq.heappush(heap, (job[1], job[0], i))  # 0:소요시간(이게 우선순위의 기준), 1:요청시간, 2:인덱스
                checked = True
        # 만약 현재 작업 종료시점에서 시작될 수 있는 작업이 없으므로 시간 더해서 다음 while 로 넘어가기
        if not checked:
            prev_t += 1
            continue
        # prev_t에서 실행가능한 것 중 소요시간이 최소인 것을 뽑는다.
        selected_job = heapq.heappop(heap)
        # 지금 추가한 작업의 소요시간만큼, 다음에 참고할 '기존 작업 종료시간(prev)'을 더해준다.
        prev_t += selected_job[0]
        # 업데이트한 prev(지금까지의 작업 종료시점) 에서 방금 get 한 친구의 요청시점(job[0])을 빼준다. 이는 해당 작업의 대기시간. 이를 총 대기시간에 더해줌
        wait_sum += (prev_t - selected_job[1])
        # 추가한 작업 jobs 리스트에서 제거하기
        jobs.remove([selected_job[1], selected_job[0]])

    # 총 대기시간 / 작업 수 하고 정수형으로 제출
    answer = int(wait_sum/num_of_jobs)
    return answer
