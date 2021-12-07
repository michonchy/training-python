# 整数値を入力させ、その個数だけ*を、5個おきに空白（スペース）を入れて表示するプログラムを作成せよ。
# 入力値が0以下の値の場合は何も書かなくてよい。
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

def graph(n):
    if n <= 0:
        return ""
    ind_number = ""
    for i in range(n):
        if i % 5 == 0 and i != 0 :
            ind_number += " "
        ind_number += "*"
    return ind_number


if __name__ == '__main__':
    a = input("How many times do yo indicate?>>\n") 
    n = number(a)      
    print(graph(n))


