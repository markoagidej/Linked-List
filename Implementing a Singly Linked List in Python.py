# Task 1 Implement the Node class to represent individual nodes in the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Task 2 Implement the SinglyLinkedList class with methods for insertion, deletion, and traversal.

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, data, position):
        # New node creation
        new_node = Node(data)
        # If there is nothing in the list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # If requested position is 1, new_node becomes the new head
            if (position == 1):
                new_node.next = self.head
                self.head = new_node
                return
            else:
                # Counting number of nodes in list
                node = self.head
                count = 0
                while node:
                    count += 1
                    node = node.next
                # If requested position is greater than the number of nodes in the list, new_node becomes the tail.
                if position > count:
                    self.tail.next = new_node
                    self.tail = new_node
                # Insert at requested position
                else:
                    prev_node = self.head
                    next_node = self.head.next
                    positionCountdown = position - 2
                    while positionCountdown != 0:
                        prev_node = next_node
                        next_node = next_node.next
                        positionCountdown -= 1
                    prev_node.next = new_node
                    new_node.next = next_node

    def deleteNode(self, data):
        node = self.head
        prev_node = None
        while node:
            # Searching for matching data
            if node.data == data:
                # Check if node is head
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.head = node.next
                # Check if node is tail
                if node.next is None:
                    self.tail = prev_node
                return True
            prev_node = node
            node = node.next
        return False

    # defining iterability
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def traverse(self,):
        print("Linked List Nodes:")
        for node in self:
            print(node, end=" -> ")
        print("End")

# Task 3 Test the implemented functionality by performing various operations on the linked list.

testLinkedList = SinglyLinkedList()
testLinkedList.insertNode("1",1)
testLinkedList.insertNode("2",10000)
testLinkedList.insertNode("3",2)
testLinkedList.insertNode("4",4)
testLinkedList.insertNode("5",5)
testLinkedList.deleteNode("4")
testLinkedList.traverse()
