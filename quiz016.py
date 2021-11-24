num = input("What is your number >>\n")
num = number(num)
while num !=0:
    print("numの今の値は" + str(num))
    num = input("What is your number >>\n")
    if num == 0:
        break
        
print("End")