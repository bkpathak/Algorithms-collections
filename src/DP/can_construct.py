"""
Can the word be constructed from the array of the words?

Complexity:
m = target.length
n = array.length
Time: O(n *m * m(slicing the string))
Space: O(m * m) -> Since we need to slice the word each time
"""


def can_construct(target, array):
    if target == "":
        return True

    for word in array:
        if target.startswith(word) and can_construct(target[len(word):], array):
            return True
    return False


"""
Time: O(n * m * m )
Space: O(m * m)
"""


def can_construct_memo(target, array, memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in array:
        if target.startswith(word) and can_construct_memo(target[len(word):], array):
            memo[target] = True
            return memo[target]

    memo[target] = False

    return memo[target]


if __name__ == "__main__":
    assert can_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee"]) is False
