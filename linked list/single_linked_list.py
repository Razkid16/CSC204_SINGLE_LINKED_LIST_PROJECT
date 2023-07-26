from nodes import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

    #Method to display the maximum and minimum data in the single linked list:
    def find_max(self):
        if self.head is None:
            return None

        current = self.head
        max_data = current.data
        while current:
            if current.data > max_data:
                max_data = current.data
            current = current.next
        return max_data

    def find_min(self):
        if self.head is None:
            return None

        current = self.head
        min_data = current.data
        while current:
            if current.data < min_data:
                min_data = current.data
            current = current.next
        return min_data

#Method that converts the single linked list into a binary search tree

    def convert_to_bst(self, lst):
        if not lst:
            return None

        mid = len(lst) // 2
        root_data = lst[mid]
        root = Node(root_data)

        root.left = self.convert_to_bst(lst[:mid])
        root.right = self.convert_to_bst(lst[mid + 1:])

        return root
#Implementing a binary search algorithm
    def binary_search(self, search_value):
        # Sort the linked list using Python's built-in sorting function
        sorted_list = []
        current = self.head
        while current:
            sorted_list.append(current.data)
            current = current.next
        sorted_list.sort()

        # Binary search on the sorted list
        low, high = 0, len(sorted_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_list[mid] == search_value:
                return mid
            elif sorted_list[mid] < search_value:
                low = mid + 1
            else:
                high = mid - 1

        return -1
#Implementing Queue using a Single Linked List

class Queue:
    def __init__(self):
        self.sll = SingleLinkedList()

    def enqueue(self, data):
        self.sll.insert(data)

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.sll.head.data
        self.sll.head = self.sll.head.next
        return data

    def display(self):
        self.sll.display()

    def is_empty(self):
        return self.sll.head is None
#Sort the Queue
    def sort_queue(self):
        # Extract elements from the queue
        elements = []
        while not self.is_empty():
            elements.append(self.dequeue())

        # Sort the elements
        elements.sort()

        # Re-enqueue the sorted elements
        for element in elements:
            self.enqueue(element)