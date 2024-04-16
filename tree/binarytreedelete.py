class Binarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,data):
        if self.data==data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binarytree(data)
        if data>self.right:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binarytree(data)

    def in_order_traversel(self):
        if self.data==None:
            return
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:  
            return self.data
        return self.left.find_min()  

    def delete(self,val):
        if val< self.data:
            if self.left:
               self.left= self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right= self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)
        return self   


def build_tree(elements):
    root=Binarytree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

numbers=[3,5,3,4,2,4,6]
numbers_tree=build_tree(numbers)
print(numbers_tree.in_order_traversal())