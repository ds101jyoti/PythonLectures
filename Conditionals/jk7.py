Maths=float(input("Enter the marks of maths: "))
Eng=float(input("Enter the marks of english: "))
Hindi=float(input("Enter the marks of hindi: "))
m=Maths
e=Eng
h=Hindi
a=m+e+h
avrg=a/3
print("Your average marks is ",int(avrg))
max_marks=300
p=int((a/max_marks*100))
print(p)
if p>=80:
    print("Congrats...Your grade is A")
    print("level 4 above agency-normalised standards")
elif p>=70:
    print("Good..Your grade is B")
    print("level 3 agency-normalised standards")
elif p>=60:
    print("Your grade is C")
    print("Level 2 below, but approaching agency standards.")
elif p>=50:
    print("Your garde is D")
    print("Level 1, well below agency standards.")
elif p>=45:
    print("Your grade is E")
    print("Level -1 too below agency level.")

elif p>=39:
    print("Your grade is R")
    print("Remedial standards.")
elif p>=34:
    print("Pass")
else:
    print("Fail")


