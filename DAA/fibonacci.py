def fib_i(n):
    a, b = 0, 1
    for _ in range(n):  # conventional placeholder variable when you don’t actually need to use the loop variable inside the loop.
        a, b = b, a + b
    return a                  # O(N),O(1)

def fib_r(n):
    if n <= 1:  #f(0),f(1)=0,1 define
        return n
    return fib_r(n - 1) + fib_r(n - 2)   # O(2^N),O(N)

method = input("Choose method ('iterative(i)' or 'recursive(r)'): ")
n = int(input("Enter a number for Fibonacci: "))

result = fib_i(n) if method == "i" else fib_r(n) if method == "r" else "Invalid method selected."
print(f"Fibonacci number at position {n} is:", result)
