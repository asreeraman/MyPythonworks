def subpart(mylist,n,subsum):
    None
def arrpart(mylists):
    if sum(mylists)%2 != 0:
        print('list cannot be partitioned' + str(sum(mylists)))
    else:
        print('list can be partitioned')
        return subpart(mylists,len(mylists),sum(mylists)/2)
        

#print(arrpart([1,2,3,4]))

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            print (str(num) + ' is not a prime number')
            break
    else:
        print (str(num) + ' is a prime number')
    
is_prime(11)