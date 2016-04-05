# Cryptiarithmetic Puzzle
#     SEND
#    +MORE
#   ------
#    MONEY
# Assign each letter a digit from 0 to 9 so the arithmetic works out.
# No two letters can be assigned same digit.
# All the occurrence of a letter must be assigned the same digit.

# Pseudocode
# Create the list of all the letters that needs to be assigned
#
# If all characters are assigned, returns true if puzzled is solved else return false.
# Otherwise consider the first unassigned character
# for every possible choice among all the digits not uses
#   make a choice and recursively try to assign the rest of the character
#   if recursion is successful return true
#   if not successful undo the choice and try another digit
# If all the digits have been tried and nothing worked return false to trigger backtracking.


class Puzzle(object):
    def __init__(self, addends_1, addends_2, sum_):
        self.addends_1 = addends_1
        self.addends_2 = addends_2
        self.sum_ = sum_
        self.letter_dict={}
        self.__create_letter_dict()

    def __create_letter_dict(self):
        """Assign None to all the letters"""
        for ch in self.addends_1 + self.addends_2 + self.sum_:
            self.letter_dict[ch] = None

    def is_puzzle_solved(self):
        carry = 0
        s_len = len(self.sum_) - 1
        addend_1_len = len(self.addends_1) - 1
        addend_2_len = len(self.addends_2) - 1
        for i in range(s_len):
            add_1_val = 0
            add_2_val = 0
            if addend_1_len - i >= 0:
                add_1_val = self.letter_dict.get(self.addends_1[addend_1_len - i])
            if addend_2_len - i >= 0:
                add_2_val = self.letter_dict.get(self.addends_2[addend_2_len - i])

            sum_val = (carry + add_1_val + add_2_val) % 10
            carry = (carry + add_1_val + add_2_val) // 10
            if self.letter_dict.get(self.sum_[s_len - i]) is not sum_val:
                return False
        if carry is not 0 and self.letter_dict.get(self.sum_[0]) is not carry:
            return False

        return True

    def assign_digit_to_letter(self, letter, digit):
        if digit in self.letter_dict.values():
            return False
        self.letter_dict[letter] = digit
        return True

    def unassign_digit_to_letter(self, letter):
        self.letter_dict[letter] = None

    def unique_letter_list(self):
        return list(self.letter_dict.keys())

    def display_letter_digit_map(self):
        for k, v in self.letter_dict.items():
            print("{0} => {1}".format(k, v))


def solve_puzzle(puzzle, letter_to_assign):
    if len(letter_to_assign) == 0:    # Base case, no more choices to make
        return puzzle.is_puzzle_solved()                            # Check if the puzzled is solve

    for digit in range(1, 10):                                             # Try all digits
        if puzzle.assign_digit_to_letter(letter_to_assign[0], digit):     # Temporarily assign digit to letter
            if solve_puzzle(puzzle, letter_to_assign[1:]):                   # Recurse if temporary assignment is success
                return True
            else:
                puzzle.unassign_digit_to_letter(letter_to_assign[0])          # Unassign if not

    return False                                                           # Trigger back track since none of the avialbe;
                                                                           # options worked

if __name__ == "__main__":
    puzzle = Puzzle("SEND", "MORE", "MONEY")
    unique_letter = puzzle.unique_letter_list()
    solve_puzzle(puzzle, unique_letter)
    puzzle.display_letter_digit_map()
