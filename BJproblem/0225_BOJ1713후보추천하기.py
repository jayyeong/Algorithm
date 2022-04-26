N = int(input())
M = int(input())
box = list(map(int,input().split()))
photo = {}


def pop():
    global photo
    temp = []
    min = 1001
    # 최솟값을 뽑고 그값과 같은 key들을 모두 모아
    for k, v in photo.items():
        if v <= min:
            min = v

    for k, v in photo.items():
        if v == min:
            temp.append(k)

    del photo[temp[0]]

for x in box:
    if x in photo: # 먼저 요소 확인
        photo[x] = photo.get(x) + 1
    else:
        if len(photo) == N: # 꽉찬경우
            pop()
            photo[x] = 1
        else:   # 중복도 없고 사진틀 개수가 남는경우
            photo[x] = 1

    #print(photo)

result = list(photo.keys())
result.sort()
print(' '.join(str(a) for a in result))