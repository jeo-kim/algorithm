# import sys
# sys.setrecursionlimit(10**6)
n,m = map(int, input().split())
chars = list(input().split())
chars.sort()
res = [0]*n
result_list = []
vowels = ["a", "e", "i", "o", "u"]

def DFS(L, start):
    if L == n:
        result = "".join(res)
        v_count = 0
        for vowel in vowels:  # 모음 나올때마다 카운팅
            v_count += result.count(vowel)
        if 1 <= v_count <= n - 2:
            result_list.append(result)
        return
    else:
        for i in range(start, m-n+L+1):
            res[L] = chars[i]
            DFS(L+1, i+1)

DFS(0, 0)

for result in result_list:
    print(result)


