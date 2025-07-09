memo = [None]*10000
memo[0] = 1
memo[1] = 1
def memo_fib(n):
    if memo[n] is not None:
        return memo[n]
    else:
        if memo[n-1] is None:
            memo[n-1] = memo_fib(n-1)
        if memo[n-2] is None:
            memo[n-2] = memo_fib(n-2)

        memo[n] = memo[n-1] + memo[n-2]
        
        return memo[n]
    
def fib(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(memo_fib(1000))