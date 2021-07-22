"""
Write a function bestSum(targetSum, numbers) that takes target sum
and array of numbers as arguments

The function should return teh array combination of shortest sum and if there is a tie
any combination can be returned

bestSum(8, [2,3,5,8])
[2, 2, 2, 2]
[3,5]
[8]

m = target sum
n = number of elements

Brute force

time
O(n) = O(n * m)
Space complexity
O(n) = O(m) * O(shortest combination length)  = O(m*2)
"""


def best_sum(target, nums):
    if target == 0:
        return []

    if target < 0:
        return None
    ans = None
    for n in nums:
        current_ans = best_sum(target - n, nums)
        if current_ans is not None:
            current_ans = [n] + current_ans
            if ans is None or len(current_ans) < len(ans):
                ans = current_ans

    return ans


def best_sum_memo(target, nums, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    ans = None

    for n in nums:
        current_ans = best_sum_memo(target - n, nums, memo)
        if current_ans is not None:
            current_ans = [n] + current_ans
            if ans is None or len(current_ans) < len(ans):
                ans = current_ans

    memo[target] = ans
    return ans


if __name__ == "__main__":
    # assert best_sum_memo(8, [2, 3, 5]) == [3, 5]
    print(best_sum_memo(1000, [1]))
