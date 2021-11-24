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

def get_hello_world_set(n):
    hello_world_set = ""
    for index in range(n):
        hello_world_set +="Hello World!\n"
    return hello_world_set
if __name__ == '__main__':
    a = input("How many times do yo indicate?>>\n") 
    n = number(a)      
    print(get_hello_world_set(n))
