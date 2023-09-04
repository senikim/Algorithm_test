# 다시 혼자 풀어보기
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100:
                # [progresses, speeds의 첫 원소의 진행률이 100% 이상이 되면 pop]
            progresses.pop(0)
            speeds.pop(0)
            count += 1
                # [배포된 기술의 수 += 1]
        else:
            if count > 0:
                answer.append(count)
                    # [앞 순서에 배치된 기술 배포가 이미 끝나서 pop이 됐으면 (count>0)]
                    # [끝난 애들을 answer값에 삽입해야 함; 뒤에 기술이 먼저 끝났다해도 앞 기술이 끝나지 않는 이상 그 시간에 끝나기 때문에]
                count = 0
                    # [count 초기화]
            time += 1
            # [첫 기술이 아직 100%가 안되면 시간 += 1]
    answer.append(count)
    return answer