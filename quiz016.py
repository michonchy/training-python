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
    
if __name__ == '__main__':
    num = None
    while num !=0:
        print("numの今の値は" + str(num))
        num = input("What is your number >>\n")
        num = int(num)
    print("End")