print("Printing Prime Numbers in between 1 & 100...\n")
for i in range(1, 101):
    flag=True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)