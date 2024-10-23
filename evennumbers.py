import threading
# Shared data structure to store sums
sums = {'even': 0, 'odd': 0}
 
# Function to calculate the sum of even numbers
def sum_even(numbers):
    global sums
    for num in numbers:
        if num % 2 == 0:
            sums['even'] += num
 
# Function to calculate the sum of odd numbers
def sum_odd(numbers):
    global sums
    for num in numbers:
        if num % 2 != 0:
            sums['odd'] += num
 
# Main function
def main():
    # Input from user: array of numbers
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    # Creating threads for summing even and odd numbers
    even_thread = threading.Thread(target=sum_even, args=(numbers,))
    odd_thread = threading.Thread(target=sum_odd, args=(numbers,))
 
    # Starting the threads
    even_thread.start()
    odd_thread.start()
 
    # Waiting for both threads to complete
    even_thread.join()
    odd_thread.join()
 
    # Output the results
    print(f"Sum of even numbers: {sums['even']}")
    print(f"Sum of odd numbers: {sums['odd']}")
 
# Driver code
if __name__ == "__main__":
    main()