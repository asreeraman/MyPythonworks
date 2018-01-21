def subpart(mylist,n,midval):
    if n<0:
        return False
    else:
        if mylist[n-1]>midval:
            return subpart(mylist,n-1,midval)
        else:
            midval=midval-mylist[n-1]
            if midval==0:
                return True
            else:
                return subpart(mylist,n-1,midval) or subpart(mylist,n-2,midval) 
        
def arrpart(mylist):
    listsum=sum(mylist)
    if listsum%2==0:
        midval=listsum/2;        
        print('partition possible ' + str(midval))
        l = subpart(mylist, len(mylist), midval)
        print(l)
    else:
        print('partition not possible')

mylist = [20,5,1,5,50,20,1,122,100,22,1,1,0,0,0,0,0,1,0,0,0,0,1]
print(mylist)
arrpart(mylist)