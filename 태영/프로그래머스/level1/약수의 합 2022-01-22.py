def solution(n):
    answer = 0
    j = 1
    while n+1 != j:
        if n % j == 0:
            print(j)
            answer += j
        j += 1

    return answer


print(solution(12))
