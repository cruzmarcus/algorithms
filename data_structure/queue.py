from collections import deque

# Create an empty queue
queue = deque()

# Add some items to the queue

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Print the queue contents
print(queue)

# Pop an item off the front of the queue
x = queue.popleft()
print(f"Popped: ", x)
print(f"Queue: ", queue)