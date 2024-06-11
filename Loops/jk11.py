num=int(input("Enter the number of rows and columns: "))
for i in range(num):
    for j in range(num):
        if i==0 or i==(num-1):
            print("*",end=' ')
        elif i == j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 

num=int(input("Enter the number of rows and columns: "))
for i in range(num):
    for j in range(num):
        if i==0 or i==(num-1):
            print("*",end=' ')
        elif j == num - i - 1:
            print("*", end=' ')
        else:
            print(' ', end=' ')
    print() 