#x=1
#y=5
#if x==1 and y<10:
 #   print("Matched")
  
#else:
 #   print("Not mathed")   

x=int(input("Enter a value for x:"))
y=int(input("Enter a value for y:"))
z=int(input("Enter a value for z:"))    
if x<y<z:
    print("branch 1",end=" ")
elif x>y>z:
    print("branch 2",end=' ')
else:
    print("branch 3",end=' ')
print("is the branch")
    
