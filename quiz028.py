# 整数値を入力させ、その値の階乗を表示するプログラムを作成せよ。
# ただし、0以下の値を入力した場合は1と表示する。
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

def keisann(n):
    if n <= 0:
        return 1
    add_number = 1
    for i in range(1,n+1):
        add_number *= i
    return add_number

if __name__ == '__main__':
    a = input("How many times do yo indicate?>>\n") 
    n = number(a)      
    print(keisann(n))
