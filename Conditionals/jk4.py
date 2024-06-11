d1=int(input("Enter the dividend: "))
d2=int(input("Enter the divisor: "))
if d2==0:
    print("divisor is", d2)
    print("can't divide by 0")
    print("run the program again and enter non zero divisor.")
elif d2==1:
    print("Dividing the number by 1 gives the same number you fool...")
elif d2!=0:
    print("the result of : ", d1,"/",d2,"is ",d1/d2)
    print("thank you.")

else:
    print("Invalid entry.")
