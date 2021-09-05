"""
Write a function `countConstruct(target, wordBank)` that accepts a target string and an array of strings.

The function should return the number of ways that the `target` can be constructed by concatenating
elements of the `wordBank` array.
"""


def count_construct(target, word_bank):
    if target == "":
        return 1

    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            total_count = total_count + count_construct(target[len(word):], word_bank)

    return total_count


if __name__ == "__main__":
    assert count_construct("abcdef", ["ab", "de", "cdef", "abc", "f"]) == 2
