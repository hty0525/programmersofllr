def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(i*x)
    return answer


# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]


print(number_generator(2, 5))
