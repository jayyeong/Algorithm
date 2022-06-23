import dis

def Func_else(n):
    if n % 2 == 0:
        return True
    else:
        return False

def Func_elif(n):
    if n % 2 == 0:
        return True
    elif n % 2 == 1:
        return False

dis.dis(Func_else)
print('---------------------------------------------------------')
dis.dis(Func_elif)
