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

        if user_choice in ('1', '2', '3', '4'):
            num_1 = get_number("Enter first number: ")
            num_2 = get_number("Enter second number: ")

            try:
                if user_choice == '1': print(f"Result: {calculator.add(num_1, num_2)}")
                elif user_choice == '2': print(f"Result: {calculator.subtract(num_1, num_2)}")
                elif user_choice == '3': print(f"Result: {calculator.multiply(num_1, num_2)}")
                elif user_choice == '4': print(f"Result: {calculator.divide(num_1, num_2)}")

            except ZeroDivisionError as error:
                print(error)
        
        elif user_choice == '5':
            print("\n--- Running Pace Calculator ---")
            for key, val in calculator.race_distances.items():
                print(f"{key}. {val[0]}")

            run_distance = input("Select Distance (1-6): ")

            if run_distance in calculator.race_distances:
                name, distance =  calculator.race_distances[run_distance]
                elapsed_time = input("Enter your time for {name} (HH:MM:SS, for example: 1:59:30): ")
