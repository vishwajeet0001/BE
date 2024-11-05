def knap(cap,items):
    items.sort(key=lambda x : x[1]/x[0], reverse=True) #(value / weight) tells us how much value we get per unit of weight for each item.
    tvalue=0

    for w,v in items:
        if cap>=w:
            tvalue+=v
            cap-=w
        else:
            tvalue+=v*(cap/w)
            break
    return tvalue

cap=int(input("capacity of bag:"))
n=int(input("enter no of items:"))

items = []
for i in range(n):
    w = float(input(f"Enter weight of item {i+1}: "))
    v = float(input(f"Enter value of item {i+1}: "))
    items.append((w, v))

print(items)
maxvalue=knap(cap,items)
print("maxvalue of the bag is:",maxvalue)

    
#O(nlogn)+O(n)
#O(n)