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

def number_count(n):
    for i in range(0,n+1):
        return(list(range(0,n+1)))
    # listにしたら改行されん。。かなしい 
if __name__ == '__main__':
    a = input("How many times do yo indicate?>>\n")
    n = number(a)
    print(number_count(n))

