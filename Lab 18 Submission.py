import threading
import time
from queue import Queue

# Create a shared queue
testQ = Queue()

# Producer function
def producer():
    for i in range(6):
        item = f"Item {i+1}"
        testQ.put(item)
        print(f"Produced: {item}")
        time.sleep(1)  # Wait 1 second between items

# Consumer function
def consumer():
    for i in range(6):
        item = testQ.get()
        print(f"Consumed: {item}")
        testQ.task_done()
        time.sleep(2)  # Wait 2 seconds between consuming

# Create threads for producer and consumer
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()

print("All items produced and consumed.")
