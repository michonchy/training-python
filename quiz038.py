# {3, 7, 0, 8, 4, 1, 9, 6, 5, 2}で初期化される大きさ10の整数型配列を宣言し、
# 最初は参照する要素番号を0とし、この参照する要素番号の配列要素の値を表示し、
# 次にその配列要素の値を次の参照する要素番号とし、
# ……を10回繰り返すプログラムを作成せよ。
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
def keisann(num):
    for i in range(10):
        num = number_list[num]
        print(num)
    return 'end'
# None表示されないようにするには？
# リターンで文字を返すとpytestがうまくいかない。。。       
 
if __name__ == "__main__":
    print(keisann(0))