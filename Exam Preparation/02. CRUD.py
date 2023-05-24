def next_possition(row, col,  direction):
    poss_dict = {"right": lambda r, c: [r, c + 1], "left": lambda r, c: [r, c - 1],
                 "up": lambda r, c: [r -1, c], "down": lambda r, c: [r + 1, c]}
    return poss_dict[direction](row, col)

bouth_numbers = 6
matrix = []

for row in range(bouth_numbers):
    tem_row = input().split(" ")
    matrix.append(tem_row)

possition = input().replace("(",'').replace(")",'')
s_row, s_col = [int(x) for x in possition.split(', ')]

while True:
    entr = input().split(", ")
    command = entr[0]
    if command == "Stop":
        break

    direction = entr[1]
    if command == "Create":
        value = entr[2]
        s_row, s_col = next_possition(s_row, s_col, direction)
        if matrix[s_row][s_col] == ".":
            matrix[s_row][s_col] = value
    elif command == "Update":
        value = entr[2]
        s_row, s_col = next_possition(s_row, s_col, direction)
        if matrix[s_row][s_col] != ".":
            matrix[s_row][s_col] = value
    elif command == "Delete":
        s_row, s_col = next_possition(s_row, s_col, direction)
        if matrix[s_row][s_col] != ".":
            matrix[s_row][s_col] = "."
    else:
        s_row, s_col = next_possition(s_row, s_col, direction)
        if matrix[s_row][s_col] != ".":
            print(matrix[s_row][s_col])

for row in matrix:
    print(*row, end='\n')




