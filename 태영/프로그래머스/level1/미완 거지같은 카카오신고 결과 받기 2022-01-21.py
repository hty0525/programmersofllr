# # 무지 -> 프로도    프로도 2  무지
# # 무지 -> 네오      네오  2  무지
# # 어피치 -> 프로도   무지  1 어피치
# # 어피치 -> 무지
# # 프로도 -> 네오
# # 무지에게 메일 프로도랑 네오 정지당했다는거 각각 1개 총 2개
# # 프로도 네오  정지 했다는 메일 1개
# # 그래서 2 1 1 0 이 나오게 됨

import collections
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2


def solution(id_list, report, k):
    answer = {}
    id_dict = {}  # 유저 리스트
    re_dict = {}  # 누가 누구 신고했는지
    revers_dict = {}
    for i in id_list:  # 신고 몇번 당했는지 딕셔너리 만듦
        id_dict[i] = []
        re_dict[i] = 0
        answer[i] = 0
        revers_dict = []

    for case in report:  # 신고 중복 확인
        # 신고한 사람  # 신고당한사람
        report_user, user = case.split()
        if user not in id_dict[report_user]:
            id_dict[report_user].append(user)
            re_dict[user] += 1
    for key, values in re_dict.items():
        if values >= k:
            print(key, values)
    return answer


solution(id_list, report, k)
