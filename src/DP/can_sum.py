"""
Time complexity: Depth of the tree can be m and each level can have n branch
O(n) = O(n^m)
Space complexity : Depth of the tree
O(n) = O(n)
"""


def can_sum(nums, target):
    # base case
    if target == 0:
        return True
    if target < 0:
        return False

    for n in nums:
        if can_sum(nums, target - n):
            return True

    return False


"""
Time complexity: Number of the nodes in the tree would be n * m
O(n) = O( n * m )
Space complexity: O(m)
"""


def can_sum_memo(nums, target, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for n in nums:
        if can_sum_memo(nums, target - n, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


if __name__ == "__main__":
    print(can_sum_memo([5, 3, 4, 7], 3500))
