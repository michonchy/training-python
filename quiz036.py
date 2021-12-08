# {3, 7, 0, 8, 4, 1, 9, 6, 5, 2}で初期化される大きさ10の整数型配列を宣言し、
# 整数値を2つ入力させ、要素番号が入力値である2つの配列要素の値の積を計算して表示する
# プログラムを作成せよ。
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
def keisann(a,b):
    x = number_list[a]
    y = number_list[b]
    return x*y
 
if __name__ == "__main__":
    n = input("What is your number >>\n")
    m = input("What is your number >>\n")
    n = number(n)
    m = number(m)
    print(keisann(n,m))