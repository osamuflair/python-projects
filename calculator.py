# A somple calculator

def add(a, b):
    return (a+b)

def sub(a, b):
    return (a-b)

def mul(a, b):
    return (a*b)

def div(a, b):
    return (a/b)

def main():
    print("Welcome to calculator")
    print("1 is Addition\n2 is Subtraction\n3 is Multiplication\n4 is Division")
    choice = input("Choose: ")

    a = float(input("First Number: "))
    b = float(input("Second Number: "))

    if choice == "1":
        print(add(a, b))
    elif choice == "2":
        print(sub(a, b))
    elif choice == "3":
        print(mul(a, b))
    elif choice == "4":
        print(div(a, b))
    else:
        print("INVALID CHOICE")
main()