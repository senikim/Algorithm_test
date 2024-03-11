def solution(my_string, overwrite_string, s):
    # return my_string.replace(my_string[s:s+len(overwrite_string)1], overwrite_string)
        # [Error : test6번 실패]
    return my_string[:s]+overwrite_string+my_string[s+len(overwrite_string):]