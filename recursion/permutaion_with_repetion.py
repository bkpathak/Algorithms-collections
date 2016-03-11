# Find the permutation of String with repetion in lexographical order
# Input : AAB
# Output : 3! / 2!(Since A is repeated two time) = 3, AAB, ABA, BBA
# Output: 4! / 2! = 12


def permutation(in_string):
    """Find the permutation of string in lexographic order."""
    if in_string is None:
        return
    # Get the count of each character
    char_count = {}
    for ch in in_string:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    # Sort the keys
    unique_char = sorted(char_count)
    count = []
    string = []
    for ch in unique_char:
        string.append(ch)
        # Store the corresponding count
        count.append(char_count[ch])
    output_string = []
    result = []
    permutation_util(string, len(in_string), count, output_string, 0, result)
    return result


def permutation_util(string, str_len, count, output_string, left, result):
    """Utility funtion to find permuataion."""
    if left == str_len:
        result.append(output_string)
        return

    # Iterate through string and print all the possible permuation till
    # the character count is not 0
    for i in range(len(string)):
        # No character left skip the loop
        if count[i] == 0:
            continue
        output_string[left] = string[i]
        # Decrease the character count
        count[i] -= 1
        permutation_util(string, count, output_string, left + 1)
        # Similar to back tracking in normal permuation where we swap again for
        # the above level
        count[i] += 1

if __name__ == "__main__":
    # Input 'AA'
    if not ["AA"] == permutation("AA"):
        print("Test Failed")

    # Input 'AAB'
    if not ["AAB", "ABA", "BAA"] == permutation("AAB"):
        print("Test Failed")
