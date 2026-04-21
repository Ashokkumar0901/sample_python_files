
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    should_accumulate = True
    f_num = float(input("Give a number: "))

    while should_accumulate:
        for i in operation:
            print(i)
        action = input("What operation you want to do: ")
        s_num = float(input("Give a second number: ")) 
        answer = operation[action](f_num, s_num)
        print(f"{f_num} {action} {s_num} = {answer}")
        choice = input(f"Type 'y' to continue calculate with {answer} or type 'n' to start a new calculation: ")

        if choice == "y":
            f_num = answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()


calculator()