def solution(N, number):
    answer = int(1e18)
    # 한 번 이상 리턴된 카운트(레벨) 값이 있으면 그것보다 더 넘은 레벨로 갈 시에는 컷해주기(백트래킹)
    opers = ["/N", "+N", "N", "-N", "*N"]

    # 본 레벨이 +N(*N)으로 넘어왔다면, -N(/N)은 안 가는게 낭비를 없애는 방법.
    def DFS(L, num, oper):
        # print(f"현재 {L, num}, {oper}")

        nonlocal N
        nonlocal answer
        nonlocal opers
        if L > 8:
            return
        elif num == N:
            answer = min(answer, L)
            return
        else:
            for i in range(len(opers)):
                new_num = 0
                if oper == 2 and i != 2 and L != 1:
                    continue
                elif i+oper == 4 and i != oper:
                    continue
                else:
                    if i == 0:
                        new_num = num*N
                    elif i == 1:
                        new_num = num-N
                    elif i == 2:
                        if str(num)[-1] != str(N):
                            continue
                        else:
                            new_num = (num-N)//10
                    elif i == 3:
                        new_num = num+N
                    elif i == 4:
                        if num%N != 0:
                            continue
                        else:
                            new_num = num//N
                print(f"현재 {L, num}, 다음 L={L+1, new_num}, {opers[i]}")
                DFS(L+1, new_num, i)

    DFS(1, number, 2)
    if answer > 8:
        answer = -1

    # print(answer)
    return answer

# 감사합니다! 하지만 1,1121같은 경우 (1 1 (1+1) 1) 로 해서 총 5개로도 만들수 있는게 아닌가요? 제가 문제를 잘못이해했나요 ㅠ


# print(solution(1,1121),7)
# print(solution(5,1010),7)
#
# #
# print(solution(6,65),4)
# print(solution(5,2),3)
print(solution(5,4),3)
# print(solution(1,1),1)
# print(solution(1,11),2)
# print(solution(1,111),3)
# print(solution(1,1111),4)
# print(solution(1,11111),5)
# print(solution(7,7776),6)
# print(solution(7,7784),5)
# print(solution(2,22222),5)
# print(solution(2,22223),7)
# print(solution(2,22224),6)
# print(solution(2,11111),6)
# print(solution(2,11),3)
# print(solution(2,111),4)
# print(solution(2,1111),5)
# print(solution(9,36),4)
# print(solution(9,37),6)
# print(solution(9,72),3)
# print(solution(3,18),3)
# print(solution(2,1),2)
# print(solution(4,17),4)