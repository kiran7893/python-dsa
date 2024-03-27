class Binarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right= None

    def  add_child(self,data):
        if data==self.data:
            return
        if data< self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binarytree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binarytree(data)
        
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    def search(self,val):
        if self.data==val:
           return True
        
        if val<self.data:
            if self.left:
               return  self.left.search(val)
            else:
                return False
            
        if val>self.data:
            if self.right:
               return self.right.search(val)
            else:
                return False
    
    def min1(self):
        elements=[]
        min=[]
        if self.left:
            elements+=self.left.min1()
        elements.append(self.data)
        if self.right:
            elements+=self.right.min1()
        min.append(elements[0])
        return min
    def max1(self):
        elements=[]
        max=[]
        if self.left:
            elements+=self.left.max1()
        elements.append(self.data)
        if self.right:
            elements+=self.right.max1()
        max.append(elements[-1])
        return max

    def sum1(self):
        elements=[]
        sum2=[]
        if self.left:
            elements+=self.left.sum1()
        elements.append(self.data)
        if self.right:
            elements+=self.right.sum1()
        sum2.append(sum(elements))
        return sum2
    
    def post_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        elements.append(self.data)
        return elements
        

def build_tree(elements):
    root=Binarytree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

numbers=[3,5,3,4,2,4,6]
numbers_tree=build_tree(numbers)
print(numbers_tree.in_order_traversal())
print(numbers_tree.search(200))
print(numbers_tree.min1())
print(numbers_tree.max1())
print(numbers_tree.sum1())
print(numbers_tree.post_order_traversal())
print(numbers_tree.pre_order_traversal())



    
