def knap(cap,weight,value,n):

    dp=[[0 for i in range(cap+1)] for j in range(n+1) ] #dp table helps us store solutions to subproblems of the 0/1 knapsack problem

    for i in range(1,n+1):
        for w in range(1,cap+1):
            if weight[i-1]<=w:
                dp[i][w]=max(dp[i-1][w], value[i-1]+dp[i-1][w-weight[i-1]])  #exclude or include

            else:
                dp[i][w]=dp[i-1][w]

    return dp[n][cap]

cap=int(input("capacity of bag:"))
n=int(input("enter no of items:"))

weight=[]
value=[]
for i in range(n):
    w = int(input(f"Enter weight of item {i+1}: "))
    v = int(input(f"Enter value of item {i+1}: "))
    weight.append(w)
    value.append(v)
    

maxvalue=knap(cap,weight,value,n)
print("maxvalue of the bag is:",maxvalue)

# tc: O(n*cap)
# sc: O(n*cap)