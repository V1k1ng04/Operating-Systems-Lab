import threading
 
# Shared data structure to store the Fibonacci sequence
fib_sequence = []
 
# Function to generate the Fibonacci series
def generate_fibonacci(n):
    global fib_sequence
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
 
# Main function
def main():
    # Input from user: number of Fibonacci numbers to generate
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
 
    # Creating the thread to generate Fibonacci numbers
    fibonacci_thread = threading.Thread(target=generate_fibonacci, args=(n,))
 
    # Starting the thread
    fibonacci_thread.start()
 
    # Waiting for the thread to complete
    fibonacci_thread.join()
 
    # Output the Fibonacci sequence after the thread finishes
    print(f"The first {n} Fibonacci numbers are: {fib_sequence}")
 
# Driver code
if __name__ == "__main__":
    main()