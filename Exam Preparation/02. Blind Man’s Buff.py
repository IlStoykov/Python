def next_possition(row, col, command):
    poss_dict = {"right":lambda r, c:[r, c + 1], "left":lambda r, c:[r, c - 1],
                 "down":lambda r, c:[r + 1, c], "up":lambda r, c:[r - 1, c]}
    return poss_dict[command](row, col)

def is_inside(row, col):
    return 0 <= row < mat_row and 0 <= col < mat_col

mat_row, mat_col = [int(x) for x in input().split(" ")]
p_row, p_col = 0, 0
matrix = []
player_counter, movе_counter = 0, 0

for row in range(mat_row):
    temp_row = input().split(" ")
    for col in range(mat_col):
        if temp_row[col] == "B":
            p_row, p_col = row, col
    matrix.append(temp_row)
while True:
    command = input()
    if command == "Finish" or player_counter == 3:
        break
    else:
        t_row, t_col = next_possition(p_row, p_col, command)
        if not is_inside(t_row, t_col) or matrix[t_row][t_col] == "O":
            continue

        p_row, p_col = t_row, t_col

        if matrix[p_row][p_col] == "P":
            player_counter += 1
            matrix[p_row][p_col] = "-"
    movе_counter += 1

print("Game over!")
print(f"Touched opponents: {player_counter} Moves made: {movе_counter}")
