"""
Recursive:
Tine:
The program branches in two in each function call, and the depth of the
function is m + n. O(n) = 2^(m +n)

Space:
The depth of the recursion is n: O(m + n) = m + n
"""


def grid_travel(m, n):
    if m == 0 and n == 0:
        return 1

    if m < 0 or n < 0:
        return 0

    return grid_travel(m - 1, n) + grid_travel(m, n - 1)


"""
Number of distinct nodes, since we need to travel all the nodes at least once
O(n) = O(m *n)

Space complexity
O(n) = O(n +m)
"""


def grid_travel_memo(m, n, memo={}):
    key = str(m) + "#" + str(n)
    if key in memo:
        return memo[key]

    if m == 0 and n == 0:
        return 1

    if m < 0 or n < 0:
        return 0

    memo[key] = grid_travel_memo(m - 1, n, memo) + grid_travel_memo(m, n - 1, memo)
    return memo[key]


def grid_travel_tab(m, n):
    table = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[m - 1][n - 1]


if __name__ == "__main__":
    print(grid_travel_tab(3, 3))
