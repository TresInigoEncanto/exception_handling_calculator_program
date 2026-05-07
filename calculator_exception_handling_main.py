from calculator_exception_handling_functionality import CalculatorProgram

def user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error! Invalid input. Please enter a number.")

def main():
    calculator = CalculatorProgram

    while True:
        print("\n--- Calculator and Pace Finder ---")
        print("1. Addition | 2. Subtraction | 3. Multiplication | 4. Division | 5. Running Pace Calculator")
        user_choice = input("Enter your desired operation (1-5): ")