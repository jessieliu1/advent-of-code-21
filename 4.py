from util.util import file_to_bingo
import sys

def best_bingo_score(filename):
    bingo = file_to_bingo(filename)
    numbers = bingo[0]
    boards = bingo[1:][0]
    board_counters = []
    board_dicts = []
    for board in boards:
        dict = {}
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                dict[int(board[i][j])] = (i, j)
        board_dicts.append(dict)
        board_counters.append([[0 for x in range(len(board[0]))],[0 for x in range(len(board[0]))]])
    for num in numbers:
        for i in range(0, len(board_dicts)):
            if int(num) in board_dicts[i]:
                coord = board_dicts[i].pop(int(num))
                board_counters[i][0][coord[0]] += 1
                if board_counters[i][0][coord[0]] == 5:
                    return compute_bingo_score(board_dicts[i], int(num))
                board_counters[i][1][coord[1]] += 1
                if board_counters[i][1][coord[1]] == 5:
                    return compute_bingo_score(board_dicts[i], int(num))

def worst_bingo_score(filename):
    bingo = file_to_bingo(filename)
    numbers = bingo[0]
    boards = bingo[1:][0]
    board_counters = []
    board_dicts = []
    winners_indices = set()
    for board in boards:
        dict = {}
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                # dict{number: (row, column)}
                dict[int(board[i][j])] = (i, j)
        board_dicts.append(dict)
        # for each board, keep a list of counters per row and column for
        # marked off numbers
        board_counters.append([[0 for _ in board[0]], [0 for _ in board[0]]])
    for num in numbers:
        for i, board in enumerate(board_dicts):
            if i not in winners_indices and int(num) in board:
                (row, col) = board.pop(int(num))
                board_counters[i][0][row] += 1
                if board_counters[i][0][row] == 5:
                    winners_indices.add(i)
                    if len(winners_indices) == len(board_dicts):
                        return compute_bingo_score(board, int(num))
                board_counters[i][1][col] += 1
                if board_counters[i][1][col] == 5:
                    winners_indices.add(i)
                    if len(winners_indices) == len(board_dicts):
                        return compute_bingo_score(board, int(num))

def compute_bingo_score(board_dict, last_seen):
    print(board_dict)
    print(last_seen)
    return sum(board_dict.keys()) * last_seen

def main():
    if (sys.argv[1] == "best"):
        print(best_bingo_score(sys.argv[2]))
    else:
        print(worst_bingo_score(sys.argv[1]))

main()
