def keisann(x):
    x = int(x)
    if x == 0:
        return "zero"
    else:
        return "x"

if __name__ == "__main__":
    n = input("What is your number >>\n")
    print(keisann(n))
