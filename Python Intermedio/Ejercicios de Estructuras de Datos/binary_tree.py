class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None 
        self.right = None 


class BinaryTree:
    def __init__(self):
        self.root = None



    def insert(self, value): #Insert a new value following BST rules (left < root < right)
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)


    def search(self, value): #Return True if value exists in the tree, False otherwise
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)


    def in_order(self):
        print("In order   : ", end="")
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, current):
        if current is None:
            return
        self._in_order_recursive(current.left)
        print(current.value, end=" ")
        self._in_order_recursive(current.right)

    def pre_order(self):
        print("Pre order  : ", end="")
        self._pre_order_recursive(self.root)
        print()

    def _pre_order_recursive(self, current):
        if current is None:
            return
        print(current.value, end=" ")
        self._pre_order_recursive(current.left)
        self._pre_order_recursive(current.right)

    def post_order(self):
        print("Post order : ", end="")
        self._post_order_recursive(self.root)
        print()

    def _post_order_recursive(self, current):
        if current is None:
            return
        self._post_order_recursive(current.left)
        self._post_order_recursive(current.right)
        print(current.value, end=" ")


    def print_tree(self):
        if self.root is None:
            print("Tree: (empty)")
            return
        print("Tree structure:")
        self._print_recursive(self.root, prefix="", is_left=True)

    def _print_recursive(self, current, prefix, is_left):
        if current is None:
            return
        self._print_recursive(
            current.right,
            prefix + ("│   " if is_left else "    "),
            False
        )
        print(prefix + ("└── " if is_left else "┌── ") + str(current.value))
        self._print_recursive(
            current.left,
            prefix + ("    " if is_left else "│   "),
            True
        )



if __name__ == "__main__":
    bt = BinaryTree()

    print("=== Inserting: 50 30 70 20 40 60 80 ===\n")
    for val in (50, 30, 70, 20, 40, 60, 80):
        bt.insert(val)

    bt.print_tree()

    print()
    bt.in_order()
    bt.pre_order()
    bt.post_order()

    print("\n=== Search ===")
    for val in (40, 99):
        print(f"Search {val}: {'Found' if bt.search(val) else 'Not found'}")