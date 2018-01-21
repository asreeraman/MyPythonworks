from platform import node
class Node(object):
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
        self.height=1

    def leftdepth(self):
        if self.left == None:
            return 1
        else:
            i = self.left.leftdepth()
            return i+1
        
    def rightdepth(self):
        if self.right == None:
            return 1
        else:
            i = self.right.rightdepth()
            return i+1

    def depth(self):
        ld = self.leftdepth()
        rd = self.rightdepth()
        if ld>rd:
            return ld
        else:
            return rd
    def Rightrotation(self):
        print('Right rotating :'+ str(self.data))
        if self.left.right is not None:
            self.right = self.left.right
        self.left.right=self
        root=self.left
        self.left=None
        return root
    
    def Leftrotation(self):
        print('Left rotating :'+ str(self.data))
        if self.right.left is not None:
            self.left = self.right.left
        self.right.left=self
        root=self.right
        self.right=None
        return root
         
    def LRrotation(self):
        None
    def RLrotation(self):
        None
        
      
    def insertnode(self, node):
        if node.data > self.data:
            if self.right==None:
                self.right=node
                self.height=1
                return self
            else:
                self.right=self.right.insertnode(node)
                self.height=self.height +1 
        else:
            if self.left==None:
                self.left=node
                self.height=1
                return self
            else:
                self.left = self.left.insertnode(node)
                self.height= self.height +1
                return self
             
        ld= self.leftdepth()
        rd=self.rightdepth()
        if ld-rd >1:
            root=self.Rightrotation()
        elif rd-ld>1:
            root=self.Leftrotation()
        else:
            root=self
            return root
        return root
        
                
    
n0=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
n5=Node(60)

n0=n0.insertnode(n1)
n0=n0.insertnode(n2)
n0=n0.insertnode(n3)
n0=n0.insertnode(n4)
n0=n0.insertnode(n5)

print('left depth n1 : ' + str(n1.leftdepth()))
print('Right depth n1 : ' + str(n1.rightdepth()))

print('left depth n0 : ' + str(n0.leftdepth()))
print('Right depth n0 : ' + str(n0.rightdepth()))

#print('depth' + str(n1.depth()))
