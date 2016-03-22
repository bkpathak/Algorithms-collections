# N-Queen Problem
# The N-Queen problem is placing the N queen in N * N board game where the Queens doesn't attack each other according to
# the normal rule of chess.

import unittest


def is_safe(queen_position, col):
    # Queen will be under attack on the following 4 cases:
    # Case 1: On the same row
    # Case 2: On the same col
    # Case 3: On the same forward diagonal
    # Case 4: On the same backward diagonal
    for c in range(col):
        # Same Row
        if queen_position[c] == queen_position[col]:
            return False
        # Same Forward Diagonal
        if queen_position[col] - queen_position[c] == col - c:
            return False
        # Same Backward Diagonal
        if queen_position[c] - queen_position[col] == col - c:
            return False
        # No need to check for same column since we check for valid position in each column
    # Position is safe
    return True


def place_queen_util(queen_position, col):
    # If we reached the end of the column, that means we put the queen
    if col == len(queen_position):
        # The output is the row number to put the queen in each column
        print([r + 1 for r in queen_position])

    else:
        # Try placing the queen in each row of column `col` till we find valid position or we exhaust
        # all the available position
        for row in range(len(queen_position)):
            queen_position[col] = row
            # Check if the position is safe or not
            if is_safe(queen_position, col):
                # Find position in another column
                place_queen_util(queen_position, col + 1)


def place_queen(board_size):
    if board_size < 4:
        print(" Solution doesn't exists for Board Size of less then 4.")
        return

    queen_position = [None] * board_size  # List representing the position of Q
    place_queen_util(queen_position, 0)  # passed the position array and starting column
    # return queen_position


class TestNQueen(unittest.TestCase):
    def test_queen_position(self):
        board_size = [4, 5, 8]
        for board in board_size:
            queen_position = place_queen(board)
            print(queen_position)
            # Check if the position are valid or not
            for col in range(len(queen_position)):
                self.assertTrue(is_safe(queen_position, col), "Queen position are not valid for the "
                                                              "board size of {0}".format(board))


if __name__ == "__main__":
    print(place_queen(4))
    # unittest.main()