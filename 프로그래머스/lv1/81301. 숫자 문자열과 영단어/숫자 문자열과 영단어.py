def solution(s):
    answer = 0
    num = ["zero", "one", "two", "three", "four", "five", "six",
           "seven", "eight", "nine"]
    dic = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5,
          "six":6, "seven":7, "eight":8, "nine":9}
    
    for i in num:
        s = s.replace(str(i), str(dic[i]))
        
    answer = int(s)
    return answer