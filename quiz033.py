# 整数値を入力させ、1から9まで、入力値以外を表示するプログラムを作成せよ。
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

def get_rid(n):    
    num = ""
    for i in range(1,n+1):
        if i % 5 == 0:
            num += "bar"
        else:
            num += str(i)
    return num

if __name__ == '__main__':
    a = input("How many times do yo indicate?>>\n") 
    n = number(a)      
    print(get_rid(n))

    


