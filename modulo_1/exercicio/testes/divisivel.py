def multiplo_5(x):
    if x % 5 == 0:
        return True
    else:
        return False
def multiplo_7(x):
    if x % 7 == 0:
        return True
    else:
        return False
def multiplo_5_7(x):
    if multiplo_5(x) and multiplo_7(x):
        return True
    else:
        return False