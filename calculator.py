

greetings="welsignome to my calculator!!!!"

greetings2="how many variable do you want ?"


greetings=greetings.title()
greetings2=greetings2.title()

print(greetings)
print(greetings2)

vars= int(input("[max is 2]Enter the variable number: "))

if vars==1:
    print("Sorry need atleast 2 varibles to do arithmatic functions...")
elif vars==2:
    x=int(input("Enter your first number :"))
    y=int(input("Enter your second number :"))
    sign= (input("What is the arithematic function do you want perform +,-,*,/,% : "))
    if sign =='+':
        ans=x + y
        print(f"your answer :{ans}")
    elif sign=='-':
        ans=y-x
        print(f"your answer :{ans}")
    elif sign=='*':
        ans=x*y
        print(f"your answer :{ans}")
    elif sign=='/':
        ans=x/y
        print(f"your answer :{ans}")
    elif sign=='%':
        ans=x%y
        print(f"your answer :{ans}")
