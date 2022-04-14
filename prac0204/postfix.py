infix = "3+5*2/(7-2)"
stack = []
res = ''

for x in infix:
    # 피연산자(10진수 숫자)라면 바로 결과물에 넣어준다.
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            # * 나 / 보다 우선순위가 높은 것을 꺼낼 것인데, 먼저 들어간 * 이나 / 이 해당
            while stack and (stack[-1]=='*') or (stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            # 여는 괄호가 들어가 있었다면, 그 전에 넣어뒀던 연산자를 먼저 처리해서는 안 된다.
            # 여는 괄호 이후에 있는 연산자들이 우선적이기 때문에.
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            # 여는 괄호 연산자도 없애주기
            stack.pop()

# 중위식을 다 돌면서 처리가 끝난 후, 스택에 남아있는 연산자들도 pop해준다.
while stack:
    res += stack.pop()

print(res) # >>> 352*72-/+