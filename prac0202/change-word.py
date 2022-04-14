

def solution(begin, target, words):
    answer = 0
    l = len(begin)
    if target not in words:
        answer = 0
    else:
        for i in range(l):
            for j in range(len(words)):
                if words[j][i] != target[i]:
                    if words[j][i+1:l] == target[i+1:l]:
                        print(f"{target}과 {i}번째만 문자만 다른 단어: {words[j]}")





    return answer















# solution()

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
# print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
# print(solution("1234567000", "1234567899", [
#       "1234567800", "1234567890", "1234567899"]), 3)
# print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)