def solution(id_list, report, k):
    # 신고받은 사람 기준으로 분류
    r_num = [[] for x in range(len(id_list))]
    # print(r_num)
    for x in report:
        y = x.split()
        if not x in r_num[id_list.index(y[1])]:
            r_num[id_list.index(y[1])].append(x)
    # print(r_num)
    # k넘긴사람 저장
    rp = []
    for i in range(len(id_list)):
        if len(r_num[i]) >= k:
            rp.append(id_list[i])
    # print(rp)

    answer = [0 for _ in range(len(id_list))]
    for x in report:
        y = x.split()
        if y[1] in rp:
            answer[id_list.index(y[0])] += 1
    # print(answer)
    return answer