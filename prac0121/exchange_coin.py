def exchange_coin(coin_list: list, total: int) -> int:

    candidates = set()
    min_count = 2147000

    def DFS(L, coin, now_sum):

        if now_sum == total:
            candidates.add(L-1)
            return
        elif now_sum > total:
            return

        else:
            now_sum += coin
            for coin in coin_list:
                DFS(L+1, coin, now_sum)

    DFS(0, 0, 0)

    print(min(candidates))
    return min(candidates)

exchange_coin([1,2,5], 15)

# a = [1,2,5]
# m = 15
# res =
#
# def DFS(L, sum):
#     if sum>m:
#         return
#     if sum == m:
#         if L < res:
#             res = L
#     else:
#         for i in range(n):
#
#             DFS(L+1,sum + a[i])


