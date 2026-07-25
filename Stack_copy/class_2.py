class Stack:
    def __init__(self) -> None:
        self.elements: list = []

    def isEmpty(self) -> bool:
        return self.elements == []

    def push(self, element) -> None:
        self.elements.append(element)

    def pop(self) -> int:
        return self.elements.pop()

    def peek(self) -> list:
        return self.elements[::-1]

    def size(self) -> int:
        return len(self.elements)

    def __str__(self) -> None:
        for i in reversed(self.elements):
            print(f"|{i}|")

if __name__ == '__main__':
    
    stack = Stack()

    for i in range(5):
        stack.push(i)

    print(stack)
    stack.pop()
    print(stack)
    