#Question 1
def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string
  
input_string = "hello"
print(reverse_string(input_string))

#Question 2
class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("dequeue from an empty queue")
        return self.stack_out.pop()

q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  
print(q.dequeue())  

#Question 3
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
      
    def append(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if self.head is None:
            raise ValueError("List is empty")

        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  
