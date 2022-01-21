import math

# ㅁㄴ어라ㅣㄴ어ㅣ 문제가 지금 소수로나옴 1.222ㄹ 이런거 ㅠ


# def solution(n):
#     if math.sqrt(n)**2 == n: 뭔차이일까 .. 시부럴..!
#         return int(int(math.sqrt(n)+1)**2)
#     else:
#         return -1

def solution(n):
    if int(math.sqrt(n))**2 == n:
        return int(int(math.sqrt(n)+1)**2)
    else:
        return -1


#def solution(x): return int(math.sqrt(x)+1)**2 if int(math.sqrt(x))**2 == x else -1


print(solution(3))
