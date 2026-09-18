class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None


# Binary tree
class Tree:
    def __init__(self) -> None:
        self.root: Node = None

    def addNode(self, value) -> None:
        new_node: Node = Node(value)
        if self.root is None:
            self.root = new_node
            
        else:
            current_root = self.root
            while True:
                if value < current_root.value:
                    if current_root.left is None:
                        current_root.left = new_node
                        break
                    current_root = current_root.left

                elif value > current_root.value:
                    if current_root.right is None:
                        current_root.right = new_node
                        break
                    current_root = current_root.right

                else:
                    print(f"{value} is already in the tree.")
                    break
    
    def inOrder(self) -> None:
        """ root -> left -> right """

        def goThrought(node: Node) -> None:
            if node is None:
                return

            else:
                goThrought(node.left)
                print(node.value, end=" ")
                goThrought(node.right)
        
        goThrought(self.root)
        print()

    def inOrder_2(self, node: Node) -> None:
            if node is None:
                return
    
            else:
                self.inOrder_2(node.left)
                print(node.value, end=" ")
                self.inOrder_2(node.right)

    def postOrder(self) -> None:
        """ left -> right -> root """

        def goThrought(node: Node) -> None:
            if node is None:
                return
        
            else:
                goThrought(node.left)
                goThrought(node.right)
                print(node.value, end=" ")
                
        goThrought(self.root)
        print()    

    def postOrder_2(self, node: Node):
        if node is None:
            return
        
        else:
            self.postOrder_2(node.left)
            self.postOrder_2(node.right)
            print(node.value, end=" ")

    def preOrder(self) -> None: 
        """ root -> left -> right """

        def goThrought(node: Node) -> None:
            if node is None:
                return
            
            else:
                print(node.value, end=" ")
                goThrought(node.left)
                goThrought(node.right)
                    
        goThrought(self.root)
        print()    

    def preOrder_2(self, node: Node) -> None:
        if node is None:
            return

        else:
            print(node.value, end=" ")
            self.preOrder_2(node.left)
            self.preOrder_2(node.right)

def minimum(node) -> Node:
    while node.left:
        node = node.left
    return node

def maximun(node: Node) -> Node:
    while node.right:
        node = node.right
    return node

def delNode(root_node: Node, value) -> Node:
    if root_node is None:
        pprint(f"{value} isn't in the tree.")
        return root_node

    if root_node.value == value:
        if not root_node.left and not root_node.right:
            return None
 
        elif root_node.left is None and root_node.right:
            return root_node.right

        elif root_node.left and root_node.right is None:
            return root_node.right

        else:
            successor = minimum(root_node.right)
            root_node.value = successor.value
            root_node.right = delNode(root_node.right, successor.value)

    elif value < root_node.value:
        root_node.left = delNode(root_node.left, value)

    elif value > root_node.value:
        root_node.right = delNode(root_node.right, value)

    return root_node

def search(root_node: Node, value) -> Node:
    level = 0
    if root_node is None:
        print(f"{value} isn't in the tree.")
        return root_node

    if root_node.value == value:
        return root_node

    elif value < root_node.value:
        return search(root_node.left, value)

    elif value > root_node.value:
        return search(root_node.right, value)

def height(root_node: Node):
    if root_node is None:
        return -1
    else:
        return 1 + max(height(root_node.left), height(root_node.right))

def size(root_node: Node):
    if root_node is None:
        return 0
    else:
        return 1 + size(root_node.left) + size(root_node.right)

tree = Tree()
 
tree.addNode(10)
tree.addNode(5)
tree.addNode(3)
tree.addNode(16)
tree.addNode(8)
tree.addNode(19)
tree.addNode(1)

print("****************************")
print("In Order:")
tree.inOrder() # out: 1 3 5 8 10 16 19 

print("Post Order:")
tree.postOrder() # out: 1 3 8 5 19 16 10

print("Pre Order:")
tree.preOrder() # out: 10 5 3 1 8 16 19

print("****************************")
print(f"Mininum: {minimum(tree.root).value}") # out: 1
print(f"Maximun: {maximun(tree.root).value}") # out: 19

print("****************************")
print(f"Height: {height(tree.root)}") # out: 3
print(f"Size: {size(tree.root)}") # out: 7

delNode(tree.root, 19)
delNode(tree.root, 10)

print("****************************")
print(f"Search value: {search(tree.root, 16).value}") # out: 16
search(tree.root, 10)

print("****************************")
print("In Order:")
tree.inOrder()  # out: 1 3 5 8 16
