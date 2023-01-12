from collections import defaultdict
def solution(s):
    answer = []
    temp = defaultdict(int)
    tmp = ''
    for i in range(len(s)):
        if s[i] != '{' and s[i] != '}' and s[i] != ',':
            
            if s[i+1] != '{' and s[i+1] != '}' and s[i+1] != ',':
                tmp += s[i]
            else:
                tmp += s[i]
                temp[int(tmp)] += 1
                tmp = ''
                
    temp = sorted(temp.items(), key = lambda x : x[1], reverse = True)
    
    for i in temp:
        answer.append(i[0])
    return answer