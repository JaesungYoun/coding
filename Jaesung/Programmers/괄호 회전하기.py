from collections import deque

def check(s):
    stack = []
    for i in s:
        if i == "(" or i =="{" or i == "[":
            stack.append(i)
        else:
            if stack:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
            else:
                return 0
    return 1 if not stack else 0


def solution(s):
    answer = 0
    
    bracket = deque(s)
    
    for _ in range(len(s)):
        bracket.rotate(-1)
        if check(bracket):
            answer += 1
    
    
    
    return answer