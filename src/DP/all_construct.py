""""
Write a function `allConstruct(target, wordbank)` that accepts a target string and array of
the strings.

The function should return a 2D array containing all the ways that the 'target' can be
constructed by concatenating elements of the 'wordBank' array.
"""


def all_construct(target, array):
    if target == "":
        return [[]]

    result = []
    for word in array:
        if target.startswith(word):
            suffix_ways = all_construct(target[len(word):], array)
            target_ways = map(lambda arr: arr.insert(0, word), suffix_ways)
            map(lambda arr: result.append(arr), target_ways)
    return result


if __name__ == "__main__":
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))






