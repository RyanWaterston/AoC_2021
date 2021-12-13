import re

BOARD_SIZE = 5

def check_winner(board, drawn_nums):
    for row in range(BOARD_SIZE):
        if set(board[row]) - set(drawn_nums) == set():
            return True

    for col in range(BOARD_SIZE):
        col_nums = [board[i][col] for i in range(BOARD_SIZE)]
        if set(col_nums) - set(drawn_nums) == set():
            return True
    return False

with open("/home/rwr/advent/day4/input.txt", "r") as input_file:
    line = input_file.readline()
    boards = []
    numbers = line.split(",")
    input_file.readline()
    
    line = input_file.readline()
    while line:
        board = [[0 for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
        for row in range(BOARD_SIZE):
            board[row] = re.split("\s+", line.strip())
            line = input_file.readline()
        boards.append(board)
        line = input_file.readline()

    drawn_nums = []
    bingo_total = 0
    n = 0
    winner = -1
    board_wins = []
    while len(board_wins) < len(boards) and n < len(numbers):
        drawn_nums.append(numbers[n])
        n += 1
        for board_idx, board in enumerate(boards):
            if board_idx not in board_wins and check_winner(board, drawn_nums):
                board_wins.append(board_idx)

    for row in range(BOARD_SIZE):
        bingo_total += sum(map(int, set(boards[board_wins[-1]][row]) - set(drawn_nums)))
    print(f"Winning Board: {boards[winner]}")
    print(f"Bingo Total: {bingo_total}")
    print(f"Answer: {bingo_total * int(drawn_nums[-1])}")
