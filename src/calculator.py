def fun1(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def fun2(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x,y,z):
    total_sum = x + y + z
    return total_sum

def fun5(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def fun6(x, y):
    return x ** y

def fun7(x, y):
    if y == 0:
        raise ValueError("Cannot modulo by zero.")
    return x % y

def average(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")
    return sum(numbers) / len(numbers)

def variance(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")
    mean = average(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    return variance(numbers) ** 0.5


# Example usage demonstrating all functions
if __name__ == "__main__":
    print("Basic Arithmetic Operations")
    f1_op = fun1(2, 3)
    print(f"Addition (2 + 3): {f1_op}")
    
    f2_op = fun2(10, 3)
    print(f"Subtraction (10 - 3): {f2_op}")
    
    f3_op = fun3(4, 5)
    print(f"Multiplication (4 * 5): {f3_op}")
    
    f4_op = fun4(f1_op, f2_op, f3_op)
    print(f"Sum of three ({f1_op} + {f2_op} + {f3_op}): {f4_op}")
    
    f5_op = fun5(20, 4)
    print(f"Division (20 / 4): {f5_op}")
    
    f6_op = fun6(2, 8)
    print(f"Power (2^8): {f6_op}")
    
    f7_op = fun7(17, 5)
    print(f"Modulo (17 % 5): {f7_op}")
    
    print("\nStatistical Operations")
    numbers = [2, 4, 6, 8, 10]
    print(f"Numbers: {numbers}")
    print(f"Average: {average(numbers)}")
    print(f"Variance: {variance(numbers)}")
    print(f"Standard Deviation: {standard_deviation(numbers):.4f}")

