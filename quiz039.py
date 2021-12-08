# {3, 7, 0, 8, 4, 1, 9, 6, 5, 2}で初期化される大きさ10の整数型配列を宣言し、
# 最初は参照する要素番号を0とする。
# この参照する要素番号の配列要素の値から次の要素番号の配列要素の値を引いた値を表示し、
# 参照する要素番号を1増やす。
# この手順を9回繰り返すプログラムを作成せよ。
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
def keisann(n):
    num = 0
    for i in range(n):
        num = number_list[i]-number_list[i+1]
        print(num)
    return None
 
if __name__ == "__main__":
    print(keisann(9))