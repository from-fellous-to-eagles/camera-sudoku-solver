from collections import deque

BOARD_DIM = 9
BLOCK_DIM = 3
VALID_SUM = 45
EMPTY_CELL = 0


def display_board(board):
    """Pretty prints a sudoku grid"""
    for row in board:
        print(row)


def flattened_block(block):
    return [n for row in block for n in row]


def valid_row(array):
    """
    return true if array contains all numbers
    from 1 to BOARD_DIM without repetition
    """
    return len(array) == BOARD_DIM and set(array) == {1, 2, 3, 4, 5, 6, 7, 8, 9}


def valid_block(block):
    """
    return true if the block contains all numbers
    from 1 to 9 once
    """
    return valid_row(flattened_block(block))


def retrieve_block(board, i, j):
    """
    returns the block to which the number
    at the (i,j) position belongs
    """
    block_i = (i // BLOCK_DIM) * BLOCK_DIM
    block_j = (j // BLOCK_DIM) * BLOCK_DIM
    block = []
    for i in range(block_i, block_i + BLOCK_DIM):
        block_row = []
        for j in range(block_j, block_j + BLOCK_DIM):
            block_row.append(board[i][j])
        block.append(block_row)
    return block


def retrieve_column(board, j):
    """
    return column at position j
    """
    return [board[i][j] for i in range(BOARD_DIM)]


def valid_sum(array):
    """
    return true if sum of column or row is 45
    """
    return sum(array) == VALID_SUM


def contains_duplicate(array):
    """
    return true if row/column/block contain duplicates
    """
    filtered_array = list(filter(lambda n: n != 0, array))
    return len(set(filtered_array)) != len(filtered_array)


def valid_board(board):
    """
    return true if the board is correctly solved, false otherwise
    """
    for i in range(0, BOARD_DIM):
        if not valid_row(board[i]):
            return False
    for j in range(0, BOARD_DIM):
        if not valid_row(retrieve_column(board, j)):
            return False
    for i in range(0, BOARD_DIM, 3):
        for j in range(0, BOARD_DIM, 3):
            if not valid_block(retrieve_block(board, i, j)):
                return False
    return True


def next_case(i, j):
    """Returns next cell to visit during solving iteration """
    if j == BOARD_DIM - 1:
        return i + 1, 0
    else:
        return i, j + 1


def solve(board):
    """Return solved board
    Proceeds with Backtrack to solve the board and returns it completed
    """
    backtrack_queue = deque()
    i, j = 0, 0
    cur_val = 1
    while i < BOARD_DIM and j < BOARD_DIM:
        if board[i][j] == EMPTY_CELL:
            board[i][j] = cur_val
            while contains_duplicate(board[i]) or contains_duplicate(retrieve_column(board, j)) or contains_duplicate(
                    flattened_block(retrieve_block(board, i, j))):
                cur_val += 1
                board[i][j] = cur_val
            if cur_val == 10:
                # dead end, must go a step back
                board[i][j] = EMPTY_CELL
                i, j = backtrack_queue.pop()
                cur_val = board[i][j] + 1
                board[i][j] = EMPTY_CELL
            else:
                backtrack_queue.append((i, j))
                cur_val = 1
                i, j = next_case(i, j)
        else:
            i, j = next_case(i, j)

    return board
