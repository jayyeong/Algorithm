import sys
alpabat = [0 for _ in range(27)]

writing = sys.stdin.readlines()

for line in writing:
    l = list(line.rstrip())
    for s in l:
        if s != ' ':
            alpabat[ord(s) - 97] += 1

maxi = max(alpabat)
for i in range(len(alpabat)):
    if alpabat[i] == maxi:
        print(chr(i + 97),end='')