def solution(my_string):
    answer = ''
    string = []
    for s in my_string:
        string.append(s)
    answer = ''.join(reversed(string))
    return answer