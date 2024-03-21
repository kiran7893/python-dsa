#ascii Value
print(ord('m'))

#implementing hash function

class Hashtable:
    def __init__(self,size):
        self.size=size
        self.arr=[None for i in range(self.size)]
    
    def hash_function(self,key):
        h=0
        for  char in key:
            h+=ord(char)
        return h%self.size  
    
    
    
t=Hashtable(100)
t.arr
    
