def solution(s: str):
    s = str(s)
    keyword = {"zero": "0", "one": "1", "two": "2", "three": "3",  "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": 8, "nine": "9"}
    word = s
    for i in keyword:
        if s.find(i) >= 0:
            word = word.replace(str(i), str(keyword[i]))

    answer = int(word)
    # 마지막에 int로 숫자로 해줘야 오류안뜸 ㅠ

    return answer


s = "14fiveone5three"

print(solution(s))
