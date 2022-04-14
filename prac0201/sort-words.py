import sys

n = int(sys.stdin.readline())
words = set()
for i in range(n):
    words.add(input().rstrip())

words = list(words)
words.sort()
words.sort(key=lambda x: len(x))

for word in words:
    print(word)
