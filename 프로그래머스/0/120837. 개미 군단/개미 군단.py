# 장군 : 5, 병정 :3, 일개미 :1 의 공격력
def solution(hp):
    if hp%5 != 0:
        a = hp%5
        n1 = (hp-a)/5
        if a%3 != 0 :
            b = a%3
            n2 = (a-b)/3
            if b!=0:
                n3 = b
                return n1+n2+n3
            return n1+n2
        else:
            m1 = a/3
            return n1+m1
    else :
        return hp/5
    
    