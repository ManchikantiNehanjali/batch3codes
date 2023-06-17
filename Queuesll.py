class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        new_node=Node(data)
        if self.front is None:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
    def dequeue(self):
        if self.front is None:
            print("Queue is empty. Can't perform dequeue operation")
        else:
            dequeue_ele=self.front.data
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            return dequeue_ele
    def display(self):
        n=self.front
        if n is None:
            print("Queue is empty")
        while n is not None:
            print(n.data,end=">")
            n=n.next
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            return self.front.data
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.display()
        
