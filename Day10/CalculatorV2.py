#Calcualtor 
import os
def clear():
    os.system('cls')
#TODO - ADD
def add(n1,n2):
    return n1+n2

#TODO - Subtract
def subtract(n1,n2):
    return n1-n2

#TODO - Multiple
def multiply(n1,n2):
    return n1*n2

#TODO - Divide
def divide(n1,n2):
    return n1/n2

Opereations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def symbol():
    for symbol in Opereations:
        print(symbol)
def Calcualtor():        
    num1 = float(input("What's the first number?: "))
    symbol()
    Shouldcontinue=True
    while Shouldcontinue:       
        operation_symbol = input("Pick an operation from the line above: ")
        num2= float(input("What's the next number?: "))        
        calculation_function = Opereations[operation_symbol]#(num1, num2)
        answer = calculation_function(num1, num2)       
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a newcalcualton: ") =="y":
             symbol()
             num1 =answer
        else:
            clear()
            Calcualtor()
Calcualtor()
# elif operation_symbol == "-":
#     calculation_function = Opereations[operation_symbol]#(num1, num2)
#     answer = calculation_function(num1, num2)
# elif operation_symbol == "*":
#     calculation_function = Opereations[operation_symbol]#(num1, num2)
#     answer = calculation_function(num1, num2)
# else:
#     calculation_function = Opereations[operation_symbol]#(num1, num2)
#     answer = calculation_function(num1, num2)
# answer(num1, num2)
    
