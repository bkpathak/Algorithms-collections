"""
Given the array of the num and the target, return the combination of the number
that can generate the target.
https://leetcode.com/problems/combination-sum/

Recursive
Time Complexity:
O(n) = O(m * n ^ m)
Space Complexity
O(n) = O(m)

Memoized
Time: O(n) = O(m *n *m)
Space: O(n) = O(m * m)
"""


def how_sum(nums, target):
    if target == 0:
        return []

    if target < 0:
        return None

    for n in nums:
        ans_so_far = how_sum(nums, target - n)
        if ans_so_far is not None:
            return [n] + ans_so_far

    return None


def how_sum_memo(nums, target, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for n in nums:
        ans_so_far = how_sum_memo(nums, target - n, memo)
        if ans_so_far is not None:
            memo[target] = [n] + ans_so_far
            return memo[target]

    memo[target] = None
    return None


def how_sum_pick(nums, target, ans):
    if target == 0:
        return True

    if target < 0:
        return False

    for n in nums:
        if how_sum_pick(nums, target - n, ans):
            ans.append(n)
            return True


def helper(nums, target):
    ans = []
    how_sum_pick(nums, target, ans)
    return ans


if __name__ == "__main__":
    print(how_sum_memo([2, 3, 5, 7], 45))
