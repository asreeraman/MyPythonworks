'''
Created on Dec 6, 2017

@author: u930281
'''

#tuples
def ds1():
    t={'124f2'}
    a=set('124f,2')
    
    for n in a:
        print(n)
    print(t)
    print(a)
    print('********************************')
    l=[(1,2),(3,4),(1,2,3)]
    print(l)
    for i in l:
        if len(i) >=3:
            print(i[2])
        #for j in i:
         #   print(j)
        
        # to iterate items in dictionary, use dict.items(). This will rerurn the key values as tuples
    
def numdict(list1):
    numd={}
    for i in list1:
        if not numd:
            numd={i%10:[i]}
        else:          
            if i%10 in numd.keys():
                temp=numd[i%10]
                temp.append(i)
                numd.update({i%10:temp})
            else:
                numd.update({i%10:[i]})
#Learn this syntax d = { k : v for k,v in d.iteritems() if v}
    return numd;

def eliminatedup():
    d={1:10,2:20,3:30,4:40,5:40}
    t={v for k,v in d.items() if v>20}
    print(t)
    


comploop()
#print(numdict([10,11,21,12,20,30,99,109,209,39,49]))