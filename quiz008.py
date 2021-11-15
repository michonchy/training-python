def number(x):
    x = int(x)
    if x > 0:
        return "positive"
    else:
        return None


n = input("What is your number>>\n")
print(number(n))
