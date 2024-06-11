j=0
while(j<50):
    print("Hello world!")
    j+=10

j=25
while (25<=j<=30):
    print("Temp variable =", j)
    j=j+1

a=1.0
for j in range(1,4):
    a=a*3
print(a)
print(j)

for j in "abcde":
    print(j,end=" ")
    if j=="c":
        break