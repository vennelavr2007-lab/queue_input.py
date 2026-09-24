queue = []
for i in range(3):
    x = input("Enter element: ")
    queue.append(x)
print("Queue:", queue)
removed = queue.pop(0)
print("Removed:", removed)
print("Queue after removal:", queue)

OUTPUT:
Enter element: 3
Enter element: 4
Enter element: 5
Queue: ['3', '4', '5']
Removed: 3
Queue after removal: ['4', '5']
