def is_number(x):
    if not x.isnumeric() and not x.startswith("-"):
        return False
    return True

def number(x):
    if is_number (x):
        return "整数値を入力してください。"
    return int(x)

if __name__ == '__main__':
    n = input("What is your number >>\n")
    print(number(n))
