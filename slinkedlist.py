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
        else:
            new_node.next=self.head
            self.head=new_node

    def insertatend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head =new_node 
            return
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next
        current_node.next=new_node

    def insertatindex(self,data,index):
        new_node=Node(data)
        if self.head is None:
            return
        if index==0:
            new_node.next=self.head
            self.head=new_node
        current_node=self.head
        position=0
        while(current_node):
            if position == index-1:
                new_node.next=current_node.next
                current_node.next=new_node
            
            current_node=current_node.next
            position=position+1
    
    def removeat(self,index):
        if self.head==None:
            return
        
        if index==0:
            self.head=self.head.next
        
        current_node=self.head
        position=0
        while(current_node):
            if position ==index-1:
                current_node.next=current_node.next.next
            current_node=current_node.next
            position=position+1
    

    def length(self):
        position=0
        current_node=self.head
        while(current_node):
            current_node=current_node.next
            position=position+1
        print(position)  

    def removebegin(self):
        if  self.head==None:
            return
        else:
            self.head=self.head.next

    def removelast(self):
        if self.head is None:
            return
 
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
 
        current_node.next = None

    def printrev(self):
        current_node=self.head
        list2=[]
        while(current_node)  :
            list2.append(current_node.data)
            current_node=current_node.next
        while(list2):
            temp=list2.pop()
            print(temp)
    def indefof(self,data):
        current_node=self.head
        position=0
        while (current_node):
            if current_node.data==data:
                print(position)
            current_node=current_node.next
            position=position+1
    def insert_after_val(self,data,data1):
        
        current_node=self.head
        position=0
        while (current_node):
            if current_node.data==data:
                new_node=Node(data1)
                new_node.next=current_node.next
                current_node.next=new_node
                
            current_node=current_node.next
            position=position+1
    def printLL(self):
        current_node=self.head
        while(current_node):
            print(current_node.data)
            current_node=current_node.next
    

if __name__=="__main__":
    list1 =Linkedlist()
    list1.insertatbegin(1)
    list1.insertatbegin(2)
    list1.insertatend(3)
    list1.printLL()
    print("-------------")
    list1.insertatindex(5,3)
    list1.printLL()
    list1.removeat(3)
    print("-------------")
    list1.printLL()
    print("-------------")
    list1.length()
    print("-------------")
    list1.removebegin()
    list1.printLL()
    print("-------------")
    list1.removelast()
    list1.printLL()
    list1.insertatbegin(1)
    list1.insertatbegin(2)
    list1.insertatend(3)
    print("-------------")
    list1.printrev()
    print("-------------")
    list1.printLL()
    print("-------------")
    list1.indefof(3)
    print("-------------")
    list1.indefof(1)
    list1.insert_after_val(3,4)
    print("-------------")
    list1.printLL()
    list1.insert_after_val(3,5)
    print("-------------")
    list1.printLL()
    list1.insert_after_val(3,5)
    print("-------------")
    list1.printLL()
    list1.insert_after_val(1,3)
    print("-------------")
    list1.printLL()
    list1.insert_after_val(2,7)
    print("-------------")
    list1.printLL()
    list1.insert_after_val(4,5)
    print("-------------")
    list1.printLL()
    list1.insert_after_val(5,9)
    print("-------------")
    list1.printLL()