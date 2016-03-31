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
        self.letter_dict = {}
        self.assigned_digit = []
        self.__create_letter_dict()
        self.carry = 0
        self.current_row = 0

    def __create_letter_dict(self):
        """Assign None to all the letters"""
        for ch in self.addends_1 + self.addends_2 + self.sum_:
            self.letter_dict[ch] = None

    def __is_valid_pos(self,pos):
        if self.current_row == 0 and len(self.addends_1) - pos >= 0:
            return True
        if self.current_row == 1 and len(self.addends_2) - pos >= 0:
            return True
        if self.current_row == 3 and len(self.sum_) - pos >= 0:
            return True
        return False

    def is_puzzle_solved(self):
        # Return True if no carry else False
        return self.carry

    def is_assigning_digit_to_addend(self):
        if self.current_row is not 2:
            return True
        else:
            False

    def is_digit_assign(self, pos):
        if self.current_row == 0 and self.__is_valid_pos(pos) and  self.addends_1[pos] in self.letter_dict:
            self.current_row += 1
            return True
        if self.current_row == 1 and self.__is_valid_pos(pos) and  self.addends_2[pos] in self.letter_dict:
            self.current_row += 1
            return True
        if self.current_row == 2 and self.__is_valid_pos(pos) and self.addends_2[pos] in self.letter_dict:
            return True
        return False

    def  __sum_column(self, pos):
        addend_1_val = 0
        addend_2_val = 0
        addend_1_val = self.letter_dict.get(self.addends_1[pos])
        addend_2_val = self.letter_dict.get(self.addends_2[pos])
        sum_val = (addend_1_val + addend_2_val) + self.carry
        return sum_val

    def is_column_assignment_correct(self, pos):
        sum_val = self.__sum_column(pos)
        if self.letter_dict.get(self.sum_[pos]) == sum_val % 10:
            self.carry = sum_val / 10
            return True
        return False

    def is_correct_digit_used_by_other_letter(self, pos):
        sum_val = self.__sum_column(pos)
        if sum_val % 10 in self.assigned_digit:
            return True
        return False

    def assign_digit_to_letter(self, digit, pos):
        # Assign the digit to the addend of the column
        if self.current_row == 0:
            if self.letter_dict.get(self.addends_1[pos]) is None:
                self.letter_dict[self.addends_1[pos]] = digit
                self.current_row += 1
                return True
        if self.current_row == 1:
            if self.letter_dict.get(self.addends_2[pos]) is None:
                self.letter_dict[self.addends_2[pos]] = digit
                self.current_row += 1
                return True
        return False

    def assign_digit_to_sum(self, pos):



    def reset_row(self):
        self.current_row = 0

    def unassign_digit_to_letter(self, pos):
        if self.current_row == 0:
            self.letter_dict[self.addends_1[pos]] = None
        elif self.current_row == 1:
            self.letter_dict[self.addends_2[pos]] = None
        elif self.current_row == 2:
            self.letter_dict[self.sum_[pos]] = None

    def unique_letter(self):
        return list(self.letter_dict.keys())

    def display_assigned_digit(self):
        for key, val in self.letter_dict.items():
            print("{0} => {1}".format(key, val))


def solve_puzzle(puzzle, pos):
    # Base case if we reached beyond the left most char
    if pos < 0:
        return puzzle.is_puzzle_solved()

    if puzzle.is_assigning_digit_to_addend():
        if puzzle.is_digit_assign(pos):
            solve_puzzle(puzzle, pos)
        else:
            for digit in range(0, 10):
                if digit in puzzle.assigned_digit:
                    continue
                if puzzle.assign_digit_to_letter(digit, pos):
                    if solve_puzzle(puzzle, pos):
                        return True
                puzzle.unassign_digit_to_letter(pos)
            return False
    else:
        if puzzle.is_digit_assign(pos) and puzzle.is_column_assignment_correct(pos):
            puzzle.reset_row()
            if solve_puzzle(pos - 1):
                return True
        if puzzle.is_digit_assign(pos) and not puzzle.is_column_assignment_correct(pos):
            return False
        if not puzzle.is_digit_assign(pos) and puzzle.is_correct_digit_used_by_other_letter(pos):
            return False
        if not puzzle.is_digit_assign(pos) and not puzzle.is_correct_digit_used_by_other_letter(pos):
            puzzle.assign_digit_to_sum(pos)
            solve_puzzle(pos - 1)
    return False


if __name__ == "__main__":
    puzzle = Puzzle("send", "more", "money")
    letter_to_assign = puzzle.unique_letter()
    if solve_puzzle(puzzle, letter_to_assign):
        puzzle.display_assigned_digit()
    else:
        print("Puzzle is not solved.")
        puzzle.display_assigned_digit()

