# Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Points to the right neighbor
        self.prev = None  # Points to the left neighbor


class Deque:
    def __init__(self):
        self.left  = None  # Head (leftmost node)
        self.right = None  # Tail (rightmost node)
        self.size  = 0


    def push_left(self, value): # Insert a new node at the LEFT end (head)
        
        new_node = Node(value)

        if self.left is None:           
            self.left = self.right = new_node
        else:
            new_node.next = self.left   
            self.left.prev = new_node
            self.left = new_node        

        self.size += 1

    def push_right(self, value): # Insert a new node at the RIGHT end (tail).
        
        new_node = Node(value)

        if self.right is None:          
            self.left = self.right = new_node
        else:
            new_node.prev = self.right  
            self.right.next = new_node
            self.right = new_node       

        self.size += 1


    def pop_left(self): # Remove and return the value at the LEFT end (head).
        
        if self.left is None:
            raise IndexError("Queue is empty")

        value = self.left.value

        if self.left is self.right:     # Only one node left
            self.left = self.right = None
        else:
            self.left = self.left.next  
            self.left.prev = None       

        self.size -= 1
        return value

    def pop_right(self): #Remove and return the value at the RIGHT end (tail).
        
        if self.right is None:
            raise IndexError("Queue is empty")

        value = self.right.value

        if self.left is self.right:     # Only one node left
            self.left = self.right = None
        else:
            self.right = self.right.prev  
            self.right.next = None        

        self.size -= 1
        return value


    def print_deque(self): #Print the full structure from left to right.
        
        if self.left is None:
            print("Deque: []  (empty)")
            return

        result = "Deque: None <-- "
        current = self.left

        while current is not None:
            arrow = " <--> " if current.next else ""
            result += f"[{current.value}]{arrow}"
            current = current.next

        result += " --> None"
        print(result)
        print(f"Size: {self.size}  |  Left: {self.left.value}  |  Right: {self.right.value}")


if __name__ == "__main__":
    dq = Deque()

    print("=== Pushing elements ===")
    dq.push_right(10)
    dq.push_right(20)
    dq.push_right(30)
    dq.push_left(5)
    dq.push_left(1)
    dq.print_deque()

    print("\n=== Popping from right ===")
    print(f"Popped: {dq.pop_right()}")
    dq.print_deque()

    print("\n=== Popping from left ===")
    print(f"Popped: {dq.pop_left()}")
    dq.print_deque()

    print("\n=== Emptying the Deque ===")
    while dq.size > 0:
        print(f"Popped left: {dq.pop_left()}")
    dq.print_deque()

    print("\n=== Error handling ===")
    try:
        dq.pop_left()
    except IndexError as e:
        print(f"Error caught: {e}")