# Match case is moreover similar to switch statement.
# Use for Specific Conditions.
a = int(input("Enter the Number: "))

match a:# Can write in paranthesis if complex statement.
    case 1:
        print("The value is 1.")
    case 4:
        print("The value is 4.")
    case 7:
        print("The value is 7.")      
    case _: # To Write Default Case
        print("TRY NEXT TIME.")       