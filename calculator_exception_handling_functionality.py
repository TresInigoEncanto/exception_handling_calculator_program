class CalculatorProgram:
    def __init__(self):
        self.race_distances = {
            "1": ("3km", 3.0), "2": ("5km", 5.0), "3": ("10km", 10.0),
            "4": ("16km", 16.0), "5": ("Half-Marathon", 21.0975), "6": ("Marathon", 42.195)
        }
    
    def addition(self, x, y): return x + y
    
    def subtraction(self, x, y): return x - y

    def multiplication(self, x, y): return x * y
    
    def division(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Syntax Error! Cannot divide by zero.")
        return x / y