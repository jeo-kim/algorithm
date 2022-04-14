import collections
import sys

# 4
# -1 0 1 2
# 2


n = int(sys.stdin.readline().rstrip())
rel = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline().rstrip())

rel_dict = collections.defaultdict(list)

for i in range(1, n):
    rel_dict[rel[i]].append(i)
#
# print(rel_dict)

leaves = []
count = 0
if target == 0:
    print(0)


else:
    def DFS(node):
        global count
        if not rel_dict[node] or (len(rel_dict[node]) == 1 and rel_dict[node][0] == target):
            count += 1
            leaves.append(node)
            return
        else:
            for child in rel_dict[node]:
                if child == target:
                    continue
                DFS(child)

    DFS(0)
    print(count)
    print(leaves)




