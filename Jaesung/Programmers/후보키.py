from itertools import combinations 
def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])
    
    
    candi = set()
    
    
    for i in range(1,col+1):
        combi = list(combinations(range(col),i))
        
        for j in combi:
            keys = set()
            
            for r in relation:
                temp = []
                for k in j:
                    temp.append(r[k])
                keys.add(tuple(temp))
    
            if len(keys) == row: # 유일성 만족하면
                for ca in candi: # 최소성 만족하면
                    if not (set(ca) - set(j)):
                        break
                else:
            
                    candi.add(j)
    
    return len(candi)