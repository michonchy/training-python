# {3, 7, 0, 8, 4, 1, 9, 6, 5, 2}で初期化される大きさ10の整数型配列を宣言し、
# 整数値を入力させ、要素番号が入力値の配列要素の値を参照し、
# さらにその参照した値を要素番号とする配列要素の値を参照して表示するプログラムを作成せよ。
# 入力値が配列の要素の範囲外であるかどうかのチェックは省略してよい。
class InvalidError(Exception):
    pass
def is_number(x):
    if not x.isdigit():
        return False
    return True

def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

number_list = [3,7,0,8,4,1,9,6,5,2]
def keisann(a):
    x = number_list[a]
    x = number_list[x]
    return x
 
if __name__ == "__main__":
    n = input("What is your number >>\n")
    n = number(n)
    print(keisann(n))