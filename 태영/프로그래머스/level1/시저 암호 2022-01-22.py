# 숫자 계산 잘못해서... 삽질 엄청함 ㅠ
# ㅁㄴ아ㅣ러ㅏㅣㄴㅇ머ㅏㅣㅁㄹㄴ

def solution(s, n):
    answer = ""
    for i in str(s):
        if ord(i) == 32:
            answer += i
        elif ord(i) <= ord('Z'):
            if ord(i)+n > ord('Z'):
                num = (ord(i)+n) - ord('Z')
                answer += chr(ord("A")+num-1)
            else:
                answer += chr(int(ord(i))+n)
        else:
            if ord(i)+n > ord('z'):
                num = (ord(i)+n) - ord('z')
                answer += chr(ord("a")+num-1)
            else:
                answer += chr(int(ord(i))+n)
    return answer


# print("~", 126, "}", 125)
# print(ord("k"), ord('l'), ord("z"))
print(solution("aAzmlZ", 15))
# pvs~upv}yuv SU US UVS^U SVY^]U Y^] pv}suyvp~}s
