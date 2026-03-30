#elif == else if

# Program to enter in army.

Age = int(input("Enter Your Age: "))

if(Age==16 | Age<19):
    print("Can appear for NDA Exam.")
elif(Age>18 | Age<24):
    print("Can appear for CDS Exam.")
else:
    print("CAN APPEAR FOR TGC IF HAVE ENGINEERING DEGREE")        