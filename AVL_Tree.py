class Node(object):
    def __init__(self,data):
        self.right=None
        self.left=None
        self.height=1
        self.data=data
    def copy(self):
        temp = self;
        return temp

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
        rd = self.rightdepth()
        ld = self.leftdepth()
        if ld>rd:
            return ld
        else:
            return rd
    def calcheight(self):
        self.height = self.depth()
        if self.left is not None:
            self.left.calcheight()
        if self.right is not None:
            self.right.calcheight()

    def Rightrotation(self):
        root = self.left
        temp = self
        temp.left=None
        if root.right is not None:
            if root.left.data > self.left.data:
                temp.right = root.left
            else:
                temp.left = root.left
        root.right=temp
        return root
    
    def Leftrotation(self):
        root = self.right
        temp = self
        temp.right=None
        if root.left is not None:
            if root.left.data > self.left.data:
                temp.right = root.left
            else:
                temp.left = root.left
        root.left=temp
        return root
    def printtree(self):
        print(str(self.data))
        self.printnodesorgordr()
        print('asending')
        print(self.printnodesasc())
    def printnodesorgordr(self):
        if self.data is not None:
            if self.left is not None and self.right is not None:
                print(str(self.left.data) + '--'+str(self.right.data))
            elif self.left is not None and self.right is None:
                print(str(self.left.data) )
            elif self.left is None and self.right is not None:
                print(str(self.right.data) )
            if self.left is not None:
                self.left.printnodesorgordr()
            if self.right is not None:
                self.right.printnodesorgordr()
                
    def printnodesasc(self):
        if self.left is None:
            print(self.data)
        else: 
            self.left.printnodesasc()
            print(self.data)
            if self.right is not None:
                self.right.printnodesasc()
        
           
    def insertnode(self, node):
        if node.data > self.data:
            if self.right==None:
                self.right=node
                return self
            else:
                self.right=self.right.insertnode(node)
                self.calcheight()
        else:
            if self.left==None:
                self.left=node
                return self
            else:
                self.left = self.left.insertnode(node)
                self.calcheight()
        ld= self.leftdepth()
        rd= self.rightdepth()
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
n6=Node(70)
n7=Node(80)
n8=Node(90)
n9=Node(100)

n0=n0.insertnode(n1)
n0=n0.insertnode(n2)
n0=n0.insertnode(n3)
n0=n0.insertnode(n4)
n0=n0.insertnode(n5)
n0=n0.insertnode(n6)
n0=n0.insertnode(n7)
n0=n0.insertnode(n8)
n0=n0.insertnode(n9)
n0.printtree()

print('left depth Root : ' + str(n0.leftdepth()))
print('Right depth Root : ' + str(n0.rightdepth()))

#print('depth' + str(n1.depth()))