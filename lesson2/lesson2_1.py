def calculate_sum(n):
    """
    Calculate sum from 1 to n
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def main():
    # Simple variables for debugging
    name = "Student"
    age = 20
    numbers = [1, 2, 3, 4, 5]
    
    # Function call to demonstrate step-into
    result = calculate_sum(5)
    
    # Loop for demonstrating step-over
    for num in numbers:
        print(f"Processing number: {num}")
    
    # Final output
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Sum of numbers 1 to 5: {result}")

if __name__ == "__main__":
    main() # 呼叫 main function
else:
    print("這不是python直接執行")