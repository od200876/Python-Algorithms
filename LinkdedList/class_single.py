class Node:
    """ class Node """

    def __init__(self, value):
        self.value = value
        self.next = None

        
class LinkedList:
    """ class LinkedList """

    def __init__(self) -> None:
        self.head = None

    def addEnd(self, value) -> None:
        """ Add value node at the end of linked list. """

        new_node = Node(value)
        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def addFirst(self, value) -> None:
        """ Add value node at the head of linked list. """

        new_node = Node(value)
        if self.head is None:
            self.head = new_node

        else:
            self.head, self.head.next = new_node, self.head

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
                    new_node.next, previous.next = current, new_node
                    return

            else:
                previous, current = current, current.next
                nth_node += 1

    def display(self) -> None:
        """ Print all value in linked list. """

        if self.head is None:
            return None

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

    def removeNode(self, value) -> None:
        """ Remove the node of value passed as param. """

        current = self.head
        predecessor = None
        while current:
            if current.value == value:
                if predecessor is None:
                    self.head = current.next
                    return f"Value {current.value} was removed in linked list."
                
                predecessor.next = current.next
                return f"Value {current.value} was removed in linked list."

            predecessor, current = current, current.next

    def size(self) -> str:
        """ return number of node in linked list. """

        num_node = 0
        current = self.head
        while current:
            num_node += 1
            current = current.next

        return f"Size of linked list: {num_node}"

linkedlist = LinkedList()

for i in range(1, 5):
    linkedlist.addEnd(i)

for i in range(5, 10):
    linkedlist.addFirst(i)

linkedlist.insertAt(1, 10)
linkedlist.insertAt(4, 11)
print(linkedlist.searchNode(10))
print(linkedlist.size())
linkedlist.display()

linkedlist.removeNode(6)

print(linkedlist.size())
linkedlist.display()
