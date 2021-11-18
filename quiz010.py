def number(x):
    x = int(x)
    if x < 0:
        return -1*x
    else:
        return x

if __name__ == "__main__":
    n = input("What is your number >>\n")
    print(number(n))
