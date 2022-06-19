BOARD_DIM = 9
BLOCK_DIM = 3
VALID_SUM = 45


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
