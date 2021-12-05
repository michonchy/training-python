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

number_dict = {
    "1":"one","2":"two","3":"three"
}
def keisann(x):
    y = number_dict.get(x,"others")
    return y
 
if __name__ == "__main__":
    n = input("What is your number >>\n")
    print(keisann(n))
