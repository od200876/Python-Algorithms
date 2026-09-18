class Node:
    """ class Node """

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class CircularLinkedList:
    """ Class DoubleLinkedList """

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def addFirst(self, value) -> None:
        """ Add value node at the head of linked list. """

        new_node = Node(value)
        if self.head is None:
            self.head, self.tail, new_node.next = new_node, new_node, self.head
        else:
            new_node.next, self.head, self.tail.next = self.head, new_node, new_node

    def addEnd(self, value) -> None:
        """ Add value node at the end of linked list. """

        new_node = Node(value)
        if self.tail is None:
            new_node.next, self.tail, self.head = new_node, new_node, new_node
        else:
            new_node.next, self.tail.next, self.tail = self.head, new_node, new_node

    def insertAt(self, pos, value) -> None:
        """ Insert value node at pos position """ 
        new_node = Node(value)

        if self.head is None:
            new_node.next, self.head, self.tail = new_node, new_node, new_node
            return

        if pos == 1:
            new_node.next, self.head, self.tail.next = self.head, new_node, new_node
            return
    
        previous = self.head
        current = self.head.next
        nth_node = 2
        while current is not self.head:
            if nth_node == pos:
                previous.next, new_node.next = new_node, current
                return
            else:
                previous, current = current, current.next
                nth_node += 1

    def display(self) -> None:
        """ Print all value in linked list. """
        if self.head is None:
            print("List is empty.")
            return
        
        print(f"{self.head.value}", end=" ")
        current = self.head.next
        while current is not self.head:
            print(f"{current.value}", end=" ")
            current = current.next
        print()

    def searchNode(self, value) -> str:
        """ return value if found and its position. """
        if self.head is None:
            return f"Value: {value} not in list."

        current = self.head
        pos = 1
        while current is not self.head:
            if current.value == value:
                return f"Value: {current.value}, at index: {pos}"
            current = current.next
            pos += 1

        return f"Value: {value} not in list."

    def removeNode(self, value) -> str:
        """ Remove the node of value passed as param. """
        if self.head is None:
            return f"Value: {value} not in list."
        
        if self.head.value == value:
            if self.head is self.tail:
                self.head = self.tail = None
                return
            else:
                self.head, self.tail.next = self.head.next, self.head
        
        current = self.head.next
        previous = None
        while current is not self.head:
            if current.value == value:
                if self.head is self.tail:
                    self.head, self.tail = None, None
                    return f"{value} is removed."
                else:
                    previous.next = current.next
                    return f"{value} is removed."
            else:
                previous, current = current, current.next

    def size(self) -> str:
        """ return number of node in linked list. """
        if self.head is None:
            return "Size of linked list: 0"

        current = self.head.next
        num_node = 1
        while current is not self.head:
            num_node += 1
            current = current.next

        return f"Size of linked list: {num_node}"
            
linkedlist = CircularLinkedList()

for i in range(5):
    linkedlist.addFirst(i)

for i in range(5, 10):
    linkedlist.addEnd(i)

linkedlist.addFirst(20)
linkedlist.addEnd(19)
linkedlist.addFirst(40)
linkedlist.addEnd(98)
linkedlist.insertAt(1, 16)
linkedlist.insertAt(5, 13)

print(linkedlist.searchNode(98))
print(linkedlist.removeNode(4))
print(linkedlist.searchNode(4))
linkedlist.display()
print(linkedlist.size())