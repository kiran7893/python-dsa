class TreeNode():
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def print_tree(self,num):
        space = ' ' *self.get_level()*5
        print(space + self.data)
       
        if self.children:
            for child in self.children:
                child.print_tree(0)
        
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p =p.parent
        return level


root=TreeNode("1")

two= TreeNode("2")
two.add_child(TreeNode("3"))
two.add_child(TreeNode("4"))

five=TreeNode("5")
five.add_child(TreeNode("6"))
five.add_child(TreeNode("7"))

root.add_child(two)
root.add_child(five)

root.print_tree(1)
print(root.get_level())