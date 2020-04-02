# [Ǯ��-1] ���� Ȱ��
# ���̽� ���� sort : timsort
# �־��� ��� O(n logn), ��� O(n)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    answer = None
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer is None:
        answer = participant[-1]
    
    return answer


# [Ǯ��-2] - Counter Ȱ��
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
