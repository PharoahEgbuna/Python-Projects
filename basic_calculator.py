def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def subtract(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice in ['a', 'A', 'addition', 'Addition', '1']:
        print("Addition")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        add(a, b)
    elif choice in ['b', 'B', 'subtraction', 'Subtraction', '2']:
        print("Subtraction")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        subtract(a, b)
    elif choice in ['c', 'C', 'multiplication', 'Multiplication', '3']:
        print("Multiplication")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        mul(a, b)
    elif choice in ['d', 'D', 'division', 'Division', '4']:
        print("Division")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        div(a, b)
    elif choice in ['e', 'E', 'exit', 'Exit', '5']:
        print("""
    Exiting Calculator
    Thank you for your time!""")
        quit()
     