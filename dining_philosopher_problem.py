import threading
import time
import random

# Number of philosophers and forks
NUM_PHILOSOPHERS = 5

# A semaphore for each fork (chopstick)
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

# Mutex to avoid race conditions while picking up forks
mutex = threading.Lock()

def philosopher(philosopher_id):
    while True:
        # Philosopher is thinking
        print(f"Philosopher {philosopher_id} is thinking.")
        time.sleep(random.uniform(1, 3))

        # Philosopher is hungry and tries to pick up forks
        print(f"Philosopher {philosopher_id} is hungry.")
        
        # Prevent deadlock by picking up the lower numbered fork first
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % NUM_PHILOSOPHERS
        
        # To avoid deadlock, we enforce an ordering: even philosophers pick the left fork first, odd ones pick the right first.
        if philosopher_id % 2 == 0:
            # Pick up the left fork
            forks[left_fork].acquire()
            print(f"Philosopher {philosopher_id} picked up left fork {left_fork}.")
            
            # Pick up the right fork
            forks[right_fork].acquire()
            print(f"Philosopher {philosopher_id} picked up right fork {right_fork}.")
        else:
            # Pick up the right fork first for odd-numbered philosophers
            forks[right_fork].acquire()
            print(f"Philosopher {philosopher_id} picked up right fork {right_fork}.")
            
            # Pick up the left fork
            forks[left_fork].acquire()
            print(f"Philosopher {philosopher_id} picked up left fork {left_fork}.")

        # Philosopher is eating
        print(f"Philosopher {philosopher_id} is eating.")
        time.sleep(random.uniform(1, 2))

        # Philosopher puts down the forks after eating
        forks[left_fork].release()
        forks[right_fork].release()
        print(f"Philosopher {philosopher_id} put down both forks.")

        # Philosopher returns to thinking
        time.sleep(random.uniform(1, 3))

# Create and start philosopher threads
philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]

for p in philosophers:
    p.start()

# Optional: join threads (though philosophers never stop in this simulation)
# for p in philosophers:
#     p.join()
