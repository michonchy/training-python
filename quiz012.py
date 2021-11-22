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

hello_world_set = ""
a = input("How many times do yo indicate?>>\n") 
n = number(a)      
for index in range(n):
    hello_world_set +="Hello World!\n"
print(hello_world_set)
