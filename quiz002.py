class DivisionError(Exception):
    pass

def mod(x, y):
    if y==0:
        raise DivisionError("0で割ってはいけません。")
    return x % y


print(mod(12345, 7))
