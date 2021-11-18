def number(x):
    x = int(x)
    if x < 0:
        return "negative"
    elif x > 0:
        return "positive"
    else:
        return "zero"

if __name__ == "__main__":
    n = input("What is your number >>\n")
    print(number(n))
