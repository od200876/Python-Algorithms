class Node:
    """ class Node """

    def __init__(self, value) -> None:
        self.value = value
        self.previous = None
        self.next = None


class DoubleLinkedList:
    """ Class DoubleLinkedList """

    def __init__(self) -> None:
        self.head = None


    def addFirst(self, value) -> None:
        """ Add value node at the head of linked list. """

        new_node = Node(value)
        if self.head is None:
            self.head = new_node

        else:
            new_node.next, self.head.previous, self.head = self.head, new_node, new_node

    def addEnd(self, value) -> None:
        """ Add value node at the end of linked list. """

        
        new_node = Node(value)
        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next, new_node.previous = new_node, current

    def insertAt(self, pos, value) -> None:
        """ Insert value node at pos position """ 

        new_node = Node(value)
        current = self.head
        previous = None
        nth_node = 1
        while current:
            if nth_node == pos:
                if previous is None:
                    new_node.next, self.head = self.head, new_node
                    return

                else:
                    new_node.next, new_node.previous, previous.next = current, previous, new_node
                    return

            else:
                previous, current = current, current.next
                nth_node += 1

    def display(self) -> None:
        """ Print all value in linked list. """

        current = self.head
        while current:
            print(f"{current.value}", end=" ")
            current = current.next

        print()

    def searchNode(self, value) -> str:
        """ return value if found and its position. """

        current = self.head
        pos = 1
        while current:
            if current.value == value:
                return f"Value: {current.value}, at: {pos}"
            
            current = current.next
            pos += 1

    def removeNode(self, value) -> str:
        """ Remove the node of value passed as param. """

        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                    return f"Value {current.value} was removed in linked list."
                
                previous.next = current.next
                return f"Value {current.value} was removed in linked list."

            previous, current = current, current.next

    def size(self) -> str:
        """ return number of node in linked list. """

        current = self.head
        num_node = 0
        while current:
            num_node += 1
            current = current.next

        return f"Size of linked list: {num_node}"
            
linkedlist = DoubleLinkedList()

for i in range(5):
    linkedlist.addFirst(i)

for i in range(5, 10):
    linkedlist.addEnd(i)

print(linkedlist.searchNode(4))
print(linkedlist.size())
print(linkedlist.removeNode(7))
linkedlist.insertAt(1, 16)
linkedlist.insertAt(5, 13)
linkedlist.display()
