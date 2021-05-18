def fib(n, memo={}):
    print(memo)
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


if __name__ == "__main__":
    print("Starting")
    print(fib(50))
