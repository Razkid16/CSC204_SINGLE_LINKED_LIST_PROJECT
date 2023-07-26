from single_linked_list import SingleLinkedList
from single_linked_list import Queue

if __name__ == "__main__":
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    # Create a Single Linked List and insert the data
    sll = SingleLinkedList()
    for data in data_list:
        sll.insert(data)

    # Display the Single Linked List
    sll.display()
# Find the maximum and minimum values in the linked list
    max_value = sll.find_max()
    min_value = sll.find_min()
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")

    # Convert the linked list to a binary search tree
    bst_root = sll.convert_to_bst(data_list)

    # In-order traversal of the BST to display the tree
    print("\nBinary Search Tree (In-order traversal):")
    def in_order_traversal(root):
        if root:
            in_order_traversal(root.left)
            print(root.data, end=' ')
            in_order_traversal(root.right)
    in_order_traversal(bst_root)
# Test binary search
    search_value = 22
    index = sll.binary_search(search_value)
    if index != -1:
        print(f"Binary search: {search_value} found at index {index}")
    else:
        print(f"Binary search: {search_value} not found")


# Testing Queueing operations
    queue = Queue()
    for data in data_list:
        queue.enqueue(data)

    print("\nQueue:")
    queue.display()

    print("Dequeue:", queue.dequeue())

    print("Queue after dequeue:")
    queue.display()

    queue.sort_queue()
    print("\nSorted Queue:")
    queue.display()
