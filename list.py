'''
Created on Nov 16, 2017

@author: anank
'''
mylist=[4,5,1,3,7]
print('unsorted list '+ str(mylist))
mysortlist=[]
mysortlist.insert(0,[mylist[0]])
for x in range(1 , len(mylist)):
    print('x'+str(x))
    for y in range(0,len(mysortlist)):
        print('y'+str(y))
        print('mysortlist[y]'+str(mysortlist[y]))
        temp=mysortlist
        temp1=mylist
        if temp > temp1:
            mysortlist.insert(y, [mylist[x]])
        else:
            mysortlist.insert(y, [mylist[x]])
print(mysortlist)                