def all_combination(arr):
    ans = []
    helper(ans, arr, 0, [])
    return ans


def helper(ans, arr, idx, curr):
    if idx == len(arr):
        ans.append(curr.copy())
        return

    # don't choose current
    helper(ans, arr, idx + 1, curr)
    # choose current
    curr.append(arr[idx])
    helper(ans, arr, idx + 1, curr)
    curr.pop()


if __name__ == "__main__":
    print(all_combination(["a", "b", "c"]))


