S = input()
bomb = input()
stack = []
# def check():
#     if bomb in S:
#         return True
#     return False
#
# while check():
#     S = S.replace(bomb,'')
#
# if len(S) == 0:
#     print("FRULA")
# else:
#     print(S)

for s in S:
    stack.append(s)
    if s == bomb[-1]:
        if ''.join(stack[-len(bomb):]) == bomb:
            for i in range(len(bomb)):
                stack.pop()

if stack:
    for a in stack:
        print(a,end='')
else:
    print("FRULA")