def keisann(x, y):
    x, y = int(x), int(y)
    return x+y, x-y, x*y, x/y, x % y

if __name__ == "__main__":
    A = input("What is your number 1 >>\n")
    B = input("What is your number 2 >>\n")
    print(keisann(A, B))
