#!/usr/bin/env python3

def get_num_terms():
    """Prompt the user for a positive integer and return it."""
    while True:
        try:
            n = int(input("Enter how many terms of the Fibonacci sequence you want: "))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_fibonacci(n):
    """Generate a Fibonacci sequence with n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_sequence(sequence):
    """Print the Fibonacci sequence."""
    print("\nFibonacci Sequence:")
    for num in sequence:
        print(num, end=" ")
    print()  

def main():
    n = get_num_terms()
    sequence = generate_fibonacci(n)
    print_sequence(sequence)


if __name__ == "__main__":
    main()

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
