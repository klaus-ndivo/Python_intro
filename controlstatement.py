num=int(input("Enter number:"))

if num%2==0:
    print(f"{num} is an even number")
    
else:
    print(f"{num} is an odd number")
    

# create a program to check if someone can vote or not

age=int(input("Enter your age:"))

if age>=18:
    print(f"You are legible to vote")
    
#program to grade students

marks=int(input("Enter Marks"))

if marks<=100 and marks>=80:
    print("You have an A")
elif marks<=79 and marks>=60:
    print("You have a B")
elif marks<=40 and marks>=59:
    print("You have a C")
elif marks==0 and marks>=39:
    print("You have failed terribly")
else:
    print("Invalid marks entered`")
    

