class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Dlinklist:
    def __init__(self):
        self.head=None
    
    def insertatbegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            
