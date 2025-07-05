num = 1
for i in range(1, 5):  # 4 rows
    for j in range(i):  # increasing columns
        print(num, end=" ")
        num += 1
    print()  # new line after each row
