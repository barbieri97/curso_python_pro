def positivo(var1):
    if var1 >= 0:
        return True
    else:
        return False

def inteiro(var1):
    if var1 // 1 == var1:
        return True
    else:
        return False

def natural (var):
    if inteiro(var) and positivo(var):
        return True
    else:
        return False