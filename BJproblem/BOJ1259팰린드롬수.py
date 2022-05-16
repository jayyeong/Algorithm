N = 100000

def ispel(arr):
    if len(arr) <= 1:
        return True
    if arr[0] == arr[-1]:
        return ispel(arr[1:-1])
    else:
        return False

while 1:
    N = int(input())
    if N == 0:
        break
    box = list(str(N))
    if ispel(box):
        print("yes")
    else:
        print("no")