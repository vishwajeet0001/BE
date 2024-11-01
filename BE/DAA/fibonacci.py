def fib(n):

    if(n<=0):
        return 0,1
    elif n==1:
        return 1,1
    
    a,b,s=0,1,2

    for i in range(2,n+1):
        a,b=b,a+b
        s+=1

    return b,s

n=int(input("enter a no:"))
if n<0:
    print("non negative daal")

else:
    f,s=fib(n)
    print(f"no is:{f}")
    print(f"step is:{s}")

#O(1) SC O(n) TC