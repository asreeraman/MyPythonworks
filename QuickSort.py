'''
Created on Nov 17, 2017

@author: anank
'''
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

plist = [7,2,6,3,5,0,4]
print('list before' +str(plist))
quicksort(plist,0,7)
print('list after' +str(plist))

print(0.1+0.2-0.3)


