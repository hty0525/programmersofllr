# def solution(phone_number):
#     answer = ''
#     f = phone_number[-4::]
#     print(f)
#     a = str(phone_number[::-1])
#     c = str(a[0:4])
#     d = len(phone_number)-4
#     e = c+str("*"*d)
#     answer = str(e[::-1])
#     return answer


# print(solution("01033334444"))

def solution(phone_number):
    answer = str(("*"*len(phone_number))+phone_number[-4::])
    return answer


print(solution("01033334444"))
