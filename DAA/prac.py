def job(t,n,jobs):

    jobs.sort(key=lambda x:x[2],reverse=True)
    result=[None]*t

    for i in jobs:
        for j in range(min(t,i[1])-1,-1,-1):
            if result[j] is None:
                result[j]=i[0]
                break

    return result

n=int(input("enter no of job:"))
jobs=[[input("id:"),int(input("deadline:")),int(input("profit:"))] for _ in range(n)]
print(jobs)
t=int(input("enter time slot available:"))

k=job(t,n,jobs)
print(k)
