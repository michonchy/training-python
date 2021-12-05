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
    
def keisann(x, y):
    x, y = int(x), int(y)
    return int(x/y),int(x/y)*y

if __name__ == "__main__":
    A = input("What is your number 1 >>\n")
    B = input("What is your number 2 >>\n")
    print(keisann(A, B))
