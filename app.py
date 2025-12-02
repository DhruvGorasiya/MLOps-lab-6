"""
Main application demonstrating all calculator functions.
"""
import sys
import os

# Get the directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from src import calculator
from src.data_processor import DataProcessor


def main():
    print("CALCULATOR  DEMONSTRATION")


    # Basic arithmetic functions
    print("BASIC ARITHMETIC OPERATIONS:")
    print(f"fun1(10, 5) - Addition: {calculator.fun1(10, 5)}")
    print(f"fun2(10, 5) - Subtraction: {calculator.fun2(10, 5)}")
    print(f"fun3(10, 5) - Multiplication: {calculator.fun3(10, 5)}")
    print(f"fun4(2, 3, 5) - Sum of three: {calculator.fun4(2, 3, 5)}")
    print(f"fun5(10, 5) - Division: {calculator.fun5(10, 5)}")
    print(f"fun6(2, 8) - Power (2^8): {calculator.fun6(2, 8)}")
    print(f"fun7(17, 5) - Modulo (17 % 5): {calculator.fun7(17, 5)}")
    
    # Statistical functions
    print("\nSTATISTICAL OPERATIONS:")
    numbers = [2, 4, 6, 8, 10]
    print(f"Numbers: {numbers}")
    print(f"Average: {calculator.average(numbers)}")
    print(f"Variance: {calculator.variance(numbers)}")
    print(f"Standard Deviation: {calculator.standard_deviation(numbers):.4f}")
    
    # Data processor - Validate CSV test cases
    print("\nVALIDATING TEST CASES FROM DATA:")
    csv_path = os.path.join(current_dir, "data", "test_cases.csv")
    processor = DataProcessor(csv_path)
    processor.validate_operations()
    processor.print_results()



if __name__ == "__main__":
    main()
