class InvalidError(Exception):
    pass
def is_number(x):
    if x.startswith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True

def number(x):
    if not is_number (x):
        raise InvalidError("整数値を入力してください。") 
    return int(x)

if __name__ == '__main__':
    n = input("What is your number >>\n")
    print(number(n))
