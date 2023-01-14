from itertools import combinations
from collections import defaultdict
from bisect import bisect_left
# 조건과 점수를 따로 보는 것이 중요한 포인트!

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        for i in range(5):
            case = list(combinations(range(4), i)) # 조건들의 모든 경우의 수
            for c in case:
                tmp = condition.copy()
                for idx in c: # 
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score) # 이 키에 해당하는 score 모두 추가

    for value in dic.values():
        value.sort()   

    print(dic)
    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key] # 
            idx = bisect_left(target_list, target_score) # 이분탐색으로 target_score 이상인 위치의 인덱스를 구함
            count = len(target_list) - idx
        answer.append(count)      
    return answer