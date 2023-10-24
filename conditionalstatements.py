num = int(input("Enter Number: "))

if num > 0:
    print(f" {num} is a positive")
else:
    print(f" {num} is a Negative number")

Age = int(input("Enter Age to vote: "))
if Age>=18 and Age<=80:
    print("You are eligible to vote")
else:
    print("You cant vote because of a minor/old")