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


def number_array(n):
    result = ""
    for index in range(n):
        a = input("How many times do yo indicate?>>\n")
        num = number(a)
        print(str(num))
        result += "numの今の値は" + str(num)+"\n"
    return result
print(number_array(5))

