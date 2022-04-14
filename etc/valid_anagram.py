import collections

word_list = ["nocodeprogram", "promodernacog"]

# for word in word_list:
#     print(sorted(word))

def valid_anagram(words: list) -> bool:
    hash_table = collections.defaultdict(int)

    for char in words[0]:
       hash_table[char] += 1

    for char in words[1]:
        hash_table[char] -= 1

    for k, v in hash_table.items():
        if v != 0:
            return False
    return True

print(valid_anagram(word_list))