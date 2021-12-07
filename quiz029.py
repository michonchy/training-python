# 整数値を5回入力させ、それらの値の合計を表示するプログラムを繰り返しを使って作成せよ。
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

if __name__ == '__main__':
    add_number = 0
    for i in range(5):
        n = input("What is your number?>>\n")
        n = number(n)
        add_number +=n
    print(add_number)

