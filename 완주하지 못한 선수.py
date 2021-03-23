def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('')
    for i in range(len(participant)):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
    return answer


participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']
print(solution(participant, completion))
