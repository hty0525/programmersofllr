def solution(n):
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer


print(solution(123456))


# def digit_reverse(n):
# return list(map(int, reversed(str(n))))
