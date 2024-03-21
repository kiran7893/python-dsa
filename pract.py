class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insertatbegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node

    def insertatend(self,data):
        new_node=Node(data)
        current_node=self.head
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next
        current_node.next=new_node


    def insertvalues(self,list1):
        self.head=None
        for i in list1:
            self.insertatend(i)
    
    def length(self):
        current_node=self.head
        count=0
        while(current_node):
            count=count+1
            current_node=current_node.next
        print(count)    

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
 
    def remove_at(self,index):
        if self.head is None:
            return
        if index==0 :
            self.head=self.head.next
        current_node=self.head
        count=0
        while(current_node):
            if count==index-1:
                current_node.next= current_node.next.next
                break
            
            current_node=current_node.next
            count=count+1
        else:
            print("invalid index")

    def insert_at(self,data,index):
        new_node=Node(data)
        if  self.head is None:
            return
        
        if index==0:
            self.insertatbegin(data)

        position=0
        current_node=self.head
        while(current_node):
            if position==index-1:
                new_node.next=current_node.next
                current_node.next=new_node
                
                break

            position=position+1
            current_node=current_node.next
        else:
            print("invalid syntax")    





list1=Linkedlist()
list1.insertatbegin(1)
list1.insertatbegin(2)
list1.insertatend(3)
print("length")
list1.length()
list1.insertvalues([1,2,3,4,5])
list1.printLL()
print("length")
list1.length()
list1.remove_at(2)
print(".....")
list1.printLL()
print(".....")
list1.remove_at(0)
print(".....")
list1.printLL()
list1.remove_at(10)
print(".....")
list1.printLL()
print(".....")    
list1.insert_at(3,2)
list1.printLL()
print(".....")
