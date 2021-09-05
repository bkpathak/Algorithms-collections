def fib(n, memo={}):
    # print(memo)
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


def fib_tab(n):
    tab = [0 for i in range(n + 1)]
    tab[1] = 1

    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]

    return tab[n]


if __name__ == "__main__":
    print("Starting")
    print(fib_tab(50))
