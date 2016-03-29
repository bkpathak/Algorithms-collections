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
        self.sum = sum_
        self.letter_dict={}
        self.__create_letter_dict()

    def __create_letter_dict(self):
        """Assign None to all the letters"""
        for ch in self.addends_1 + self.addends_2 + self.sum_:
            self.letter_dict[ch] = None

    def is_puzzle_solved(self):
        carry = 0
        for i in range(len(self.addends_1) -1,-1,-1):
            add_1_val = self.letter_dict.get(self.addends_1[i])
            add_2_val = self.letter_dict.get(self.addends_2[i])
            sum_val = (add_1_val + add_2_val) %  10
            carry = (add_1_val + add_2_val) /  10
            if self.letter_dict.get(self.sum_[i]) is not sum_val:
                return False
        if carry is not 0 and self.letter_dict.get(self.sum_[0]) is not carry:
            return False

        return True


def is_puzzle_solved(puzzle):
    pass


def solve_puzzle(puzzle, lettter_to_assign):
    if len(lettter_to_assign) == 0:                             # Base case, no more choices to make
        return is_puzzle_solved(puzzle)                            # Check if the puzzled is solve

    for digit in range(1,10):                                   # Try all digits
        if assign_digit_to_letter(lettter_to_assign[0], digit): # Temporarily assign digit to letter
            solve_puzzle(puzzle, lettter_to_assign[1:])         # Recurse if temporary assignment is success
        else unassign_digit_to_letter(letter_to_assign[0],digit)# Unassign if not

    return False                                                 # Trigger back track since none of the avialbe;
                                                                 # options worked

