import collections

def solution(v):
    answer = []

    for i in zip(*v):
        count = collections.Counter(i)
        answer.extend([j for j in count if count[j] == 1])

    return answer