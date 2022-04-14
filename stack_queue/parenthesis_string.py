string = input(">>>")

def is_valid(s) -> str:

    opener = "("
    closer = ")"
    stack = [] # False
    for char in s:
        if char is opener:
            stack.append(char)
        elif char is closer:
            if not stack:
                return "NO"
            stack.pop()
        else:
            return "NO"
    if stack:
        return "NO"
    else:
        return "YES"
    # return not stack

# is_valid(string)
result = is_valid(string)
print(result)

assert is_valid("(())())") == "NO"
assert is_valid("(((()())()") == "NO"
assert is_valid("(()())((()))") == "YES"
assert is_valid("((()()(()))(((())))()") == "NO"
assert is_valid("()()()()(()()())()") == "YES"
assert is_valid("(()((())()(") == "NO"

assert is_valid("((") == "NO"
assert is_valid("))") == "NO"
assert is_valid("())(()") == "NO"

# assert not is_valid("{}]")  # false
# assert not is_valid("{{{{{{{{}}}}}}}")  # false