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
    while winner == -1 and n < len(numbers):
        drawn_nums.append(numbers[n])
        n += 1
        for board_idx, board in enumerate(boards):
            if check_winner(board, drawn_nums):
                winner = board_idx
                break

    if winner != -1:
        for row in range(BOARD_SIZE):
            bingo_total += sum(map(int, set(boards[winner][row]) - set(drawn_nums)))
        print(f"Bingo Total: {bingo_total}")
        print(f"Answer: {bingo_total * int(drawn_nums[-1])}")
