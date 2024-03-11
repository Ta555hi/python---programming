def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2) #
    
n = 0
print("Fibonacci sequence")
for i in range(n):    #range will start frm 0, 
    print(i)
    #fibo sequence is the sum of the preceding ones