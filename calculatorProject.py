import art

def add(n1,n2):
    return n1 + n2
# my_function = add
# print(my_function(4,2))

def sub(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

calculator = {}
calculator["+"] = add
calculator["-"] = sub
calculator["*"] = multi
calculator["/"] = div

# result = calculator["*"](n1= 5, n2= 3)
# print(result)

def calc():

    print(art.logo)
    print("welcome to the calculator project".title())

    num1 = float(input("type the first number\n").capitalize())
    operations = input("type a mathematical operator (a choice of '+', '-', '*' or '/')\n")
    num2 = float(input("type the second number\n").capitalize())


    result = calculator[operations](n1= num1, n2= num2)
    print(f"{num1} {operations} {num2} = {result}")

    continue_operations = input("the you wants to continue working with the previous result('yes':y & 'no':n )".title().lower())

    if continue_operations == "y":
        continue_calculation = True
        while continue_calculation:
            num1 = result
            operations = input("type a mathematical operator (a choice of '+', '-', '*' or '/')\n")
            num2 = float(input("type the second number\n").capitalize())
            result = calculator[operations](n1= num1, n2= num2)
            print(f"{num1} {operations} {num2} = {result}")
            continue_operations = input("the you wants to continue working with the previous result('yes':y & 'no':n )".title().lower())
            if continue_operations == "n":
                continue_calculation = False
    elif continue_operations == "n":
        print("\n"*50)
        calc()


print(calc())

