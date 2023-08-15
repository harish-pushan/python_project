


def main():
    x = int(input("Enter your square size :"))
    square(x)


def square (size):
    for i in range (size):
        print("*"*size,end="\n")

main()
