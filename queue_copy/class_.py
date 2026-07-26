class Queue:
    """ This is class Queue, it's like stack a queue stores n elements in a single-dimensional structure
        the elements are added and removed in FIFO format.
        FIFO => First in, First Out"""

    def __init__(self) -> None:
        self.elements = []

    def isEmpty(self) -> bool:
        return self.elements == []

    def enqueue(self, element) -> None:
        self.elements.append(element)

    def dequeue(self) -> None:
        print(self.elements[0])
        self.elements.remove(self.elements[0])

    def size(self) -> int:
        return len(self.elements)
    
    def __str__(self) -> str:
        return f"{self.elements}"

if __name__ == '__main__':
    queue = Queue()
    print(queue.isEmpty())

    for i in range(5):
        queue.enqueue(i)

    print(queue)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(10)
    print(queue)
    print(queue.size())