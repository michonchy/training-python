class InvalidError(Exception):
    pass
def is_number(x):
    if not x.isdigit():
        return False
    return True
def number(x):
    if not is_number(x):
        raise InvalidError("正の整数値を入力してください。")
    return int(x)

def keisann(x):
    x = number(x)
    if 5 < x < 20:
        return "OK"
    else:
        return ""

if __name__ == "__main__":
    n = input("What is your number >>\n")
    print(keisann(n))
