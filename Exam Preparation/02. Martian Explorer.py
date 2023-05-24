from typing import List


def next_step(row, col, item):
    poss_dict = {"right": lambda r, c:[r, c + 1],"left": lambda r, c:[r, c - 1],
                 "down": lambda r, c:[r + 1, c], "up": lambda r, c:[r - 1, c]}
    return poss_dict[item](row, col)
def out_of_matrix(row, col):
    return row < 0 or row >= size or col < 0 or col >=size
def in_matrix(row, col):
    if row < 0:
        row = size - 1
    elif row >= size - 1:
        row = 0
    elif col < 0:
        col = size - 1
    else:
        col = 0
    return row, col
def all_deposits(deposits):
    counter = 0
    deposit_list = ["w", "m", "c"]
    for item in deposits:
        if item in deposit_list:
            counter += 1
    if counter == len(deposit_list):
        return True
    else:
        return False

size = 6
p_row, p_col = 0, 0
matrix = []
deposits = set()
for row in range(size):
    temp_row = input().split(" ")
    for col in range(size):
        if temp_row[col] == "E":
            p_row, p_col = row, col
    matrix.append(temp_row)

commands = input().split(", ")
for item in commands:
    p_row, p_col = next_step(p_row, p_col, item)
    if out_of_matrix(p_row, p_col):
        p_row, p_col = in_matrix(p_row, p_col)
    maze_step = matrix[p_row][p_col]
    if maze_step == "R":
        print(f"Rover got broken at ({p_row}, {p_col})")
        break
    elif maze_step == "W":
        print(f"Water deposit found at ({p_row}, {p_col})")
        deposits.add("w")
    elif maze_step == "M":
        print(f"Metal deposit found at ({p_row}, {p_col})")
        deposits.add("m")
    elif maze_step == "C":
        print(f"Concrete deposit found at ({p_row}, {p_col})")
        deposits.add("c")
if all_deposits(deposits):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")