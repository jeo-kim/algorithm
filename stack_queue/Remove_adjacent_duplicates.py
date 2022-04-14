def removeDuplicates_k(s:str, k: int) -> str:
    stack = []
    count_stack = []

    for char in s:
        if len(stack) == 0:
            stack.append(char)
            count_stack.append(1)

        elif stack[-1] == char:
            dup_count = count_stack[-1]
            if dup_count < k-1:
                stack.append(char)
                count_stack.append(dup_count + 1)
            elif dup_count == k-1:
                for _ in range(k-1):
                    stack.pop()
                    count_stack.pop()

        else:
            stack.append(char)
            count_stack.append(1)

    return ''.join(stack)