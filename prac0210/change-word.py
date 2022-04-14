import collections

def solution(begin, target, words):
    n = len(begin)

    que = collections.deque()
    que.append((begin, 0))

    while que:
        word, cnt = que.popleft()

        # 타겟 발견하면 cnt 로 탐색한 레벨을 리턴
        if word == target:
            return cnt

        # 탐색을 허락할 수 있는 최대 레벨(깊이/cnt)는 words 에 포함된 친구들 개수이므로
        # 여기까지 왔는데도 답을 못 찾았다면,
        # 소모적인 탐색 그만두게 하기
        if cnt >= len(words):
            break

        # 후보 단어들 중에 다른 글자수가 1이라면 변환 가능한 단어이므로,
        # 변환 횟수인 cnt 를 +=1 하여 다음의 가능성 있는 변환을 위해 큐에 넣어 줌.
        for candidate in words:
            diff = 0
            for i in range(n):
                if word[i] != candidate[i]:
                    diff += 1
            if diff == 1:
                que.append((candidate, cnt+1))

    # 답을 찾지 못하고 while 종료시 0 리턴
    return 0


words = ["hot", "dot", "dog", "lot", "log", "cog"]
begin = "hit"
target = "cog"
print(solution(begin, target, words), 4)
print(solution(begin, target, ["hot", "dot", "dog", "lot", "log"]), 0)