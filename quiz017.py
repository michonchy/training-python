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

def number_array(n):
    result = ""
    for index in range(n):
        result += str(index) + "\n"
    return result 

if __name__ == '__main__':
    print(number_array(10))