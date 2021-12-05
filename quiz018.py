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

def number_array(n,a):
    result = ""
    for index in range(n):
        result += str(a)+"\n"
    return result

if __name__ == '__main__':
    a = input("How many times do yo indicate?>>\n")
    n = number(a)
    print(str(n))
    print(number_array(10,a))