from art import logo


def add(n1,n2):
    return n1+n2
    
def subtract (n1,n2):
    return n1-n2

def multiply (n1,n2):
    return n1*n2
    
def divide (n1,n2):
    return n1/n2
    
operations ={
   "+":add ,
   "-":subtract ,
   "*":multiply , 
   "/":divide
    
}

def calculator():
    print(logo)

    num1 = float(input("What is first number: "))
    for key in operations:
        print(key)
    should_continue = True
    
    while should_continue:
        operator = input("Pick an operation : ")
        num2 = int(input("what is next number: "))
        calculation_func = operations[operator]
        answer = calculation_func(num1, num2)
    
        print(f"{num1} {operator} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer}: or type 'n' to start a new calculation: ") == "y":
          num1 = answer
        else:
          should_continue = False
          calculator()

calculator()
