def solution(array, commands):
    answer = []
    for cmd in commands:
        li = []
        for i in range(cmd[0]-1, cmd[1]):
            li.append(array[i])
        li.sort()
        answer.append(li[cmd[2]-1])
        
    return answer
