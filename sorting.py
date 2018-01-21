def get_bub_sorted_list(mylist):
    print('Bubble sort: unsorted list ' + str(mylist))
    swap = True
    iter1 = 0
    while swap:
        swap = False
        for i in range(0,len(mylist)-1):
            iter1=iter1+1
            if mylist[i] > mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp 
                swap=True
    print('final bubble sorted list ' + str(mylist))
    print('Number of elements in list ' + str(len(mylist)))
    print('total iterations' + str(iter1))      

def get_Heap_sorted_list(mylist):
    iter1 = 0
    mysortedlist=[]
    listlen=len(mylist)
    while len(mylist)>0:
        minval = mylist[0]
        for listval in mylist:
            iter1=iter1+1
            if minval>listval:
                minval = listval
        mylist.remove(minval)
        mysortedlist.append(minval)
    print('final Heap sorted list ' + str(mysortedlist))
    print('Number of elements in list ' + str(listlen))
    print('total iterations' + str(iter1))      

def get_gen_sorted_list(mylist):
    print('mysort: unsorted list ' + str(mylist))
    iter1 = 0
    cnt = len(mylist)
    mysortlist=[mylist[0]]
    for x in range(1 , cnt):
        for y in range(0,len(mysortlist)):
            iter1=iter1+1
            if mylist[x] < mysortlist[y]  :    
                mysortlist.insert(y,mylist[x])
                break
            else:
                if y==(len(mysortlist)-1):
                    mysortlist.insert(y+1,mylist[x])
                    break 
    print('final sorted list ' + str(mysortlist))    
    print('Number of elements in list ' + str(len(mylist)))
    print('total iterations' + str(iter1))  
    
def quicksort(plist, lo, hi):
    if lo < hi:
        p=partition(plist,lo,hi)
        quicksort(plist, lo, p)
        quicksort(plist, p+1, hi)
def partition (plist,lo,hi):
    pivot = plist[hi-1]
    index=lo
    for i in range(lo , hi-1):
        if plist[i] < pivot:
            temp = plist[i]
            plist[i] = plist[index]
            plist[index]=temp
            index=index+1
         
    if plist[index]>pivot:
        temp1 = plist[index]
        plist[index] = plist[hi-1]
        plist[hi-1]=temp1
    return index


mylist = [2,7,12,2,1,6,-1,3,5,77,3,23,5,3,0,9,676,-220,-22,0,3]
get_gen_sorted_list(mylist)        
print('*********************************')
mylist = [2,7,12,2,1,6,-1,3,5,77,3,23,5,3,0,9,676,-220,-22,0,3]
get_bub_sorted_list(mylist)
print('*********************************')
mylist = [2,7,12,2,1,6,-1,3,5,77,3,23,5,3,0,9,676,-220,-22,0,3]
get_Heap_sorted_list(mylist)
print('*********************************')
mylist = [2,7,12,2,1,6,-1,3,5,77,3,23,5,3,0,9,676,-220,-22,0,3]
quicksort(mylist,0,len(mylist))
print('final Quick sorted list : ' +str(mylist))
print('Number of elements in list ' + str(len(mylist)))