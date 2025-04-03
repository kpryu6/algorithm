def solution(participant, completion):
    participant.sort()
    completion.sort()
    # 다르면 바로 출력
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # for문 안들어가면 참가자 맨 마지막 출력
    return participant[len(participant)-1]
