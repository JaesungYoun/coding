def solution(s):
    answer = []
    
    cnt = 0
    zero = 0
    while s != "1":
        tmp = ""
        for i in s:
            if i != "0":
                tmp += i
            else:
                zero += 1
        c = len(tmp)
        s = format(c, 'b')
        cnt += 1
        
        
    answer = [cnt,zero]
    return answer