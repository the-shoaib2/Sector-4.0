n = int(input("Enter Value : "))

def fib(n, dp = {}):
    if n not in dp:
        if n <= 1:
            dp[n] = n
        else:
            dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

print("Fibonacci Number is : ", fib(n))