import threading
 # Shared list to store prime numbers
prime_numbers = []
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# Function to generate prime numbers in a given range
def generate_primes(start, end):
    global prime_numbers
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
# Main function
def main():
    # Input from user: starting and ending numbers
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
 
    # Creating the thread to generate prime numbers
    prime_thread = threading.Thread(target=generate_primes, args=(start, end))
 
    # Starting the thread
    prime_thread.start()
 
    # Waiting for the thread to complete
    prime_thread.join()
 
    # Output the prime numbers after the thread finishes
    print(f"Prime numbers between {start} and {end}: {prime_numbers}")
 
# Driver code
if __name__ == "__main__":
    main()