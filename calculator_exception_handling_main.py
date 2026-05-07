from calculator_exception_handling_functionality import CalculatorProgram

def user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error! Invalid input. Please enter a number.")

