import threading
import time
import random
from queue import Queue

# Shared buffer (Queue) size
BUFFER_SIZE = 10

# Creating the buffer (queue) with a maximum size
buffer = Queue(maxsize=BUFFER_SIZE)

class Producer(threading.Thread):
    def __init__(self, name, buffer):
        threading.Thread.__init__(self)
        self.name = name
        self.buffer = buffer

    def run(self):
        while True:
            item = random.randint(1, 100)  # Produce an item
            self.buffer.put(item)  # Add item to the buffer
            print(f"{self.name} produced: {item}")
            time.sleep(2)  # Simulate time taken to produce

class Consumer(threading.Thread):
    def __init__(self, name, buffer):
        threading.Thread.__init__(self)
        self.name = name
        self.buffer = buffer

    def run(self):
        while True:
            item = self.buffer.get()  # Consume an item from the buffer
            print(f"{self.name} consumed: {item}")
            self.buffer.task_done()  # Mark the item as processed
            time.sleep(2)  # Simulate time taken to consume

# Create buffer, producers, and consumers
buffer = Queue(maxsize=BUFFER_SIZE)

# Instantiate producers and consumers
producers = [Producer(f"Producer-{i+1}", buffer) for i in range(2)]  # 2 producers
consumers = [Consumer(f"Consumer-{i+1}", buffer) for i in range(3)]  # 3 consumers

# Start the producer and consumer threads
for producer in producers:
    producer.start()

for consumer in consumers:
    consumer.start()

# Join threads (not necessary in this infinite-loop case, but for completeness)
for producer in producers:
    producer.join()

for consumer in consumers:
    consumer.join()
