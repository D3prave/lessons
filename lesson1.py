def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    
numerator = 10
denominator = 0

result = safe_divide(numerator, denominator)

if result is not None:
    print(f"The result of {numerator} / {denominator} is {result}")
else:
    print(f"Error occured during division!")