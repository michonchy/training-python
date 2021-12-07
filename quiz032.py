# 1から20まで順に表示するが、5の倍数の場合は
# 数字の代わりにbarと表示するプログラムを作成せよ。
class InvalidError(Exception):
    pass
def is_number(x):
    if x.startswith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True

def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

def multiple(n):    
    ind_number = ""
    for i in range(1,n+1):
        if i % 5 == 0:
            ind_number += "bar"
        else:
            ind_number += str(i)
    return ind_number

if __name__ == '__main__':
    print(multiple(20))

    


