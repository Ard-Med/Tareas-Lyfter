# Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.   class Node:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None 
        self.size = 0  

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top 
        self.top = new_node       
        self.size += 1
        print(f"{value} was added to the queue")

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        removed_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        print(f"{removed_value} has been processed")
        return removed_value

    def peek(self):
        if self.is_empty():
            print("The stack is empty")
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        if self.is_empty():
            print("  [ Empty stack ]")
            return

        print(f"  Stack ({self.size} element(s)):")
        print("  ┌─────────┐")

        current = self.top
        first = True
        while current is not None:
            if first:
                print(f"  │  {str(current.value):<6} │  <- TOP")
                first = False
            else:
                print(f"  │  {str(current.value):<6} │")
            current = current.next

        print("  └─────────┘")

stack = Stack()

print("=== PUSH ===")
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("\n=== PRINT STACK ===")
stack.print_stack()

print("\n=== PEEK ===")
print(f"  Current top: {stack.peek()}")

print("\n=== POP ===")
stack.pop()
stack.pop()

print("\n=== PRINT FINAL STACK ===")
stack.print_stack()

print("\n=== POP UNTIL EMPTY ===")
stack.pop()
stack.pop()
stack.pop()