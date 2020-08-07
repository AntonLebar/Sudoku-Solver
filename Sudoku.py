import math
import time

t_initial = int((time.process_time()) * 1000)


def print_board(board_array, board_size_pb):
    box_length = int(math.sqrt(board_size_pb))
    bar = ''
    for x in range(board_size_pb):
        if x % box_length == 0:
            bar += '+'
        bar += '-'
    bar += '+'

    row_str = ''
    for r_print in range(board_size_pb):
        if r_print % box_length == 0:
            row_str += bar + '\n'
        for column_print in range(board_size_pb):
            if column_print % box_length == 0:
                row_str += '|'
            row_str += str(board_array[r_print][column_print])
        row_str += '|\n'
    row_str += bar
    print(row_str)


def board_check():
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i1 in box_dict:
        if check_list != sorted(box_dict[i1].in_list):
            print(box_dict[i1].in_list)
            print('error in box', i1)
            return 1
    for i2 in col_dict:
        if check_list != sorted(col_dict[i2].in_list):
            print('error in column', i2)
            print(box_dict[i2].in_list)
            return 1
    for i3 in row_dict:
        if check_list != sorted(row_dict[i3].in_list):
            print('error in row', i3)
            print(row_dict[i3].in_list)
            return 1
    print("Board is validly solved")
    return 0


class Row:
    def __init__(self, r_init):
        self.r = r_init
        self.in_list = []


class Column:
    def __init__(self, c_init):
        self.c = c_init
        self.in_list = []


class Box:
    def __init__(self, pos_init):
        if isinstance(pos_init, tuple) is False:
            print("box position must be tuple")
        self.pos = pos_init
        self.in_list = []


class Cell:
    def __init__(self, pos):
        if isinstance(pos, tuple) is False:
            print("cell position must be tuple")
        self.pos = pos
        self.filled = False
        self.possible = []
        self.row = pos[0]
        self.column = pos[1]
        box_x_init = math.floor(pos[0] / 3)
        box_y_init = math.floor(pos[1] / 3)
        self.box = (box_x_init, box_y_init)
        # initialize cell as zero
        self.num = 0

    def fill(self, value):
        self.num = value
        self.filled = True

        row_dict[self.row].in_list.append(value)
        col_dict[self.column].in_list.append(value)
        box_dict[self.box].in_list.append(value)
        board[self.row][self.column] = value


board = [
    [0, 0, 0, 9, 0, 0, 2, 0, 6],
    [0, 6, 0, 0, 0, 7, 0, 9, 0],
    [0, 0, 3, 0, 8, 0, 5, 0, 0],
    [0, 0, 1, 0, 0, 4, 3, 0, 0],
    [0, 5, 0, 3, 0, 0, 0, 7, 0],
    [0, 0, 2, 7, 0, 9, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 6, 9, 0, 4],
    [0, 4, 7, 0, 5, 2, 0, 6, 0]
]

# board =[
#     [0,0,3,0,2,0,6,0,0],
#     [9,0,0,3,0,5,0,0,1],
#     [0,0,1,8,0,6,4,0,0],
#     [0,0,8,1,0,2,9,0,0],
#     [7,0,0,0,0,0,0,0,8],
#     [0,0,6,7,0,8,2,0,0],
#     [0,0,2,6,0,9,5,0,0],
#     [8,0,0,2,0,3,0,0,9],
#     [0,0,5,0,1,0,3,0,0]
# ]

print_board(board, 9)

# 9 boxes, rows and columns

cell_dict = {}
box_dict = {}
row_dict = {}
col_dict = {}

# initialize the row, col, and cell_dict
for i in range(9):
    row_dict[i] = Row(i)
    col_dict[i] = Column(i)
for r in range(3):
    for c in range(3):
        box_dict[(r, c)] = Box((r, c))

# initialize the cell dictionary
for r in range(9):
    for c in range(9):
        cell_dict[(r, c)] = Cell((r, c))
        # assign the cell number to the board
        cell_dict[(r, c)].num = board[r][c]

        if cell_dict[(r, c)].num > 0:
            cell_dict[(r, c)].filled = True

            # add pre-filled cells to the row, column, and box dictionaries
            row = cell_dict[(r, c)].row
            row_dict[row].in_list.append(cell_dict[(r, c)].num)

            column = cell_dict[(r, c)].column
            col_dict[column].in_list.append(cell_dict[(r, c)].num)

            box = cell_dict[(r, c)].box
            box_dict[box].in_list.append(cell_dict[(r, c)].num)

# create list of possibilities for each of the cells, check row, box and column,
# if it is a possible play, append it to cell_dict[position].possible
can_fill = True
while can_fill is True:
    can_fill = False
    for r in range(9):
        for c in range(9):
            position = (r, c)
            box_x = math.floor(position[0] / 3)
            box_y = math.floor(position[1] / 3)
            box = (box_x, box_y)

            # clear .possible list so that the list is properly updated
            cell_dict[position].possible = []
            for i in range(1, 10):
                if cell_dict[position].filled is False and i not in row_dict[r].in_list and i not in col_dict[c].in_list and i not in box_dict[box].in_list:
                    cell_dict[position].possible.append(i)

            if len(cell_dict[position].possible) == 1 and cell_dict[position].filled is False:
                val = cell_dict[position].possible[0]

                cell_dict[position].fill(val)
                can_fill = True

    # print_board(board, 9)

print_board(board, 9)
board_check()
# print('Function is done')

t_final = int((time.process_time()) * 1000)
print(t_final)
