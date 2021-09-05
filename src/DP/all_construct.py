""""
Write a function `allConstruct(target, wordbank)` that accepts a target string and array of
the strings.

The function should return a 2D array containing all the ways that the 'target' can be
constructed by concatenating elements of the 'wordBank' array.

Time Complexity: O(n ^ m)
There is no way to improve the time complexity more than this
"""


def all_construct(target, array):
    if target == "":
        return [[]]

    result = []
    for word in array:
        if target.startswith(word):
            suffix_ways = all_construct(target[len(word):], array)
            for way in suffix_ways:
                way.insert(0, word)
                result.append(way)
    return result


if __name__ == "__main__":
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(all_construct("aaaaaaaaaaz", ["aa", "aaa", "aaaa"]))
