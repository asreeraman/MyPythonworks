class Node(object):
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
        
    def leftdepth(self):
        if self.left == None or self.right == None:
            return 0
        else:
            i = self.left.leftdepth()
            return i+1
        
    def rightdepth(self):
        if self.left == None or self.right == None:
            return 0
        else:
            i = self.right.rightdepth()
            return i+1
    
    def insertleft(self,node):
            self.left = node
            print('L')
    def insertright(self,node):
            self.right = node
            print('R')
            
    def depth(self):
        ld = self.leftdepth()
        rd = self.rightdepth()
        if ld>rd:
            return ld
        else:
            return rd
    def insertnode(self, node):
        ld=self.leftdepth()
        rd=self.rightdepth()
        d=self.depth()
        if d==0:
            if self.left == None:
                self.insertleft(node)
            else:
                self.insertright(node)
        else:
            if ld<=rd:
                if not self.left == None:
                    self.left.insertnode(node)
                else:
                    self.insertleft(node)
            else:
                if not self.right == None:    
                    self.right.insertnode(node)
                else:
                    self.insertright(node)
                
    def printtree(self):
        print(self.data)


n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
n8=Node(8)
n9=Node(9)
n10=Node(10)
n11=Node(11)
n12=Node(12)
n1.insertnode(n2)
n1.insertnode(n3)
n1.insertnode(n4)
n1.insertnode(n5)
n1.insertnode(n6)
n1.insertnode(n7)
n1.insertnode(n8)
n1.insertnode(n9)
n1.insertnode(n10)
n1.insertnode(n11)
n1.insertnode(n12)
print('left depth' + str(n1.leftdepth()))
print('Right depth' + str(n1.rightdepth()))
print('depth' + str(n1.depth()))
