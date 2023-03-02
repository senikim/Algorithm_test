from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    report_id = defaultdict(set) # 신고한 사람-신고 당한 사람 딕셔너리 만들기
    report_c = defaultdict(int) # 신고 당한 횟수 딕셔너리 만들기
    
    for r in report:
        a, b = r.split()
        report_id[a].add(b)
        report_c[b] += 1
    
    for i in id_list:
        result = 0
        for j in report_id[i]:
            if report_c[j] >= k:
                result+=1
        answer.append(result)
    return answer