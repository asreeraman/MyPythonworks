'''
Created on Dec 24, 2017

@author: anank
'''
class Ttt_obj(object):
    def __init__(self):
        self.data= [[0,0,0],
               [0,0,0],
               [0,0,0]]
    def set_ttt1(self,rowpos,colpos):
        self.data[rowpos][colpos]=1
        self.print_ttt()
        return self
    def set_ttt2(self,rowpos,colpos):
        self.data[rowpos][colpos]=30
        self.print_ttt()
        return self
    def checkvictory(self):
        sumhoriz=[sum(i) for i in self.data]
        sumvert = [sum([self.data[i][j] for i in range(len(self.data))]) for j in range(len(self.data))]
        sumdiagLR=[self.data[i][i] for i in range(len(self.data))]
        sumdiagRL=[self.data[i][len(self.data) - (i+1)] for i in range(len(self.data))]
        
        if (3 in sumhoriz or 90 in sumhoriz) or (3 in sumvert or 90 in sumvert) or (3 == sum(sumdiagLR) or 90 == sum(sumdiagLR)) or (3 == sum(sumdiagRL) or 90 == sum(sumdiagRL)) :    
            return True
                                       
    def print_ttt(self):
        row=''
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == 1: 
                    temp ='X' 
                elif self.data[i][j] == 30:
                    temp ='O'
                else:
                    temp = '-'
                row += '  '+ temp
            row+='\n'
        print('-------------')
        print(row)        
    def start_tictactoe(self):
        t=0;
        winloss=True
        ttt=Ttt_obj()
        while t<=(len(self.data[0])+1):#checking the horizontal length of ttt matrix. Total number of play will be this +1
            ##PLAYER 1
            verpos,colpos = input("Player1: Enter row and column position : ").split()
            while ttt.data[int(verpos) -1][int(colpos) -1] != 0:
                verpos,colpos = input("Player1: Enter a different location : ").split()
            ttt=ttt.set_ttt1(int(verpos)-1,int(colpos)-1)
                
            winloss=ttt.checkvictory()
            if winloss:
                print('Player 1 won!!!')
                break
            ##PLAYER 2
            if t>=(len(self.data[0])+1):
                break
            verpos,colpos = input("Player2: Enter row and column position : ").split()
            while ttt.data[int(verpos)-1][int(colpos)-1] != 0:
                    verpos,colpos = input("Player2: Enter a different location : ").split()
            ttt=ttt.set_ttt2(int(verpos)-1,int(colpos)-1)
            winloss=ttt.checkvictory()
            if winloss:
                print('Player 2 won!!!')
                break
            t+=1
        if not winloss:    
            print('Match draw!!!')    

ttt=Ttt_obj()
ttt = ttt.start_tictactoe()


def printloop():
    mylist= [[1,2,3],
             [4,5,6],
             [7,8,9]]
    sumhoriz=[sum(i) for i in mylist]
    sumdiagLR=[mylist[i][i] for i in range(len(mylist))]
    sumdiagRL=[mylist[i][len(mylist) - (i+1)] for i in range(len(mylist))]
    sumvert = [sum([mylist[i][j] for i in range(len(mylist))]) for j in range(len(mylist))]
    print(str(sumdiagLR))
    print(str(sumdiagRL))         
    print(str(sumhoriz))
    print(str(sumvert))
    

#printloop()
        
        
    