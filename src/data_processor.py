import csv
import os
import sys

# Get the project root directory
current_file = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file))
sys.path.insert(0, project_root)

from src import calculator


class DataProcessor:
    """
    Processes and validates calculator operations from CSV files.
    """
    
    def __init__(self, csv_file):
        
        self.csv_file = csv_file
        self.results = []
    
    def load_test_cases(self):
        test_cases = []
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    test_cases.append(row)
            return test_cases
        except FileNotFoundError:
            print(f"Error: File {self.csv_file} not found.")
            return []
    
    def validate_operations(self):
        """
        Validate all operations from CSV file.
        
        Returns:
            list: Results of validation with pass/fail status.
        """
        test_cases = self.load_test_cases()
        self.results = []
        
        operation_map = {
            'addition': calculator.fun1,
            'subtraction': calculator.fun2,
            'multiplication': calculator.fun3,
            'division': calculator.fun5,
            'power': calculator.fun6,
            'modulo': calculator.fun7,
        }
        
        for test in test_cases:
            operation = test['operation']
            num1 = float(test['num1'])
            num2 = float(test['num2'])
            expected = float(test['expected_result'])
            
            try:
                if operation in operation_map:
                    result = operation_map[operation](num1, num2)
                    status = "PASS" if abs(result - expected) < 0.001 else "FAIL"
                else:
                    status = "UNKNOWN"
                    result = None
                
                self.results.append({
                    'operation': operation,
                    'num1': num1,
                    'num2': num2,
                    'expected': expected,
                    'actual': result,
                    'status': status
                })
            except Exception as e:
                self.results.append({
                    'operation': operation,
                    'num1': num1,
                    'num2': num2,
                    'expected': expected,
                    'actual': None,
                    'status': 'ERROR',
                    'error': str(e)
                })
        
        return self.results
    
    def print_results(self):
        print("DATA VALIDATION RESULTS")
        for result in self.results:
            print(f"Operation: {result['operation']:12} | Input: ({result['num1']:5}, {result['num2']:5}) | Expected: {result['expected']:6} | Actual: {result['actual']:6} | Status: {result['status']}")
   

if __name__ == "__main__":
    # Process test cases from CSV
    data_dir = os.path.join(project_root, "data")
    csv_path = os.path.join(data_dir, "test_cases.csv")
    processor = DataProcessor(csv_path)
    processor.validate_operations()
    processor.print_results()
