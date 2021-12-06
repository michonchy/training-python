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

def keisann(x):
    x = number(x)
    if -10 > x :
        return "range1"
    elif -10 <= x < 0 :
        return "range2"
    elif 0 <= x :
        return "range3"

if __name__ == "__main__":
    n = input("What is your number >>\n")
    print(keisann(n))
