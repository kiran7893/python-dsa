class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def inser_at_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next
        
        current_node.next=new_node


    def printll(self):
        current_node=self.head
        while(current_node):
            print(current_node.data )
            current_node=current_node.next


if __name__ == "__main__":
    llist =Linkedlist()
    llist.inser_at_begin(["1","2"])
    llist.inser_at_begin("2")
    llist.inser_at_begin(3)
    llist.insert_at_end(4)
    llist.insert_at_end(8)
    llist.printll()
