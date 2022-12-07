def solution(s):

    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        s_list = []
        for j in range(len(s) // i + 1):
            if s[i * j: i * (j + 1)] != '':
                s_list.append(s[i * j: i * (j + 1)])

        temp = s_list[0] # 반복되는지 확인할 문자
        temp_str = "" # 길이 측정을 위한 압축된 문자열
        count = 1# 문자가 반복하는 횟수

        for k in range(1, len(s_list)):
            if temp == s_list[k]:
                count += 1
            else:
                if count > 1:
                    temp_str += str(count)
                temp_str += temp
                temp = s_list[k]
                count = 1

        if count > 1:
            temp_str += str(count)
        temp_str += temp

        answer = min(answer, len(temp_str))

    return answer