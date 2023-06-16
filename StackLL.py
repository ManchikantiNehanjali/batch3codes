class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        if self.head is None:
            print("Stack is empty. Can't perform pop operation.")
        else:
            pop_data=self.head.data
            self.head=self.head.next
            return pop_data
    def peek(self):
        if self.head is None:
            print("Stack is empty")
        else:
            return self.head.data
    def display(self):
        if self.head is None:
            print("Stack is empty")
        else:
            n=self.head
            while(n is not None):
                print(n.data,end=">")
                n=n.next
