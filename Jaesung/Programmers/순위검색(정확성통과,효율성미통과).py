from collections import defaultdict

def solution(info, query):
    answer = [0] * len(query)
    p_info = defaultdict(list)
    
    for idx,person in enumerate(info):
        temp = []
        for i in person.split(" "):
            p_info[idx].append(i)
    for qdx,q in enumerate(query):
        for person in range(len(p_info)):
            j = 0
            for idx,i in enumerate(q.split(" ")):
                if i == '-':
                    continue
                if i == 'and':
                    j += 1
                    continue
                
                if idx == len(q.split(" ")) - 1:
                    j += 1
                    if int(p_info[person][j]) < int(i):
                        break
                else:
                    if p_info[person][j] != i:
                        break
            else:
                answer[qdx] += 1 
            
    return answer