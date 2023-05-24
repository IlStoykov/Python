def next_possition(row, col, command):
    poss_dict = {"right":lambda r, c:[r, c + 1], "left":lambda r, c:[r, c - 1],
                 "down":lambda r, c:[r + 1, c], "up":lambda r, c:[r -1, c]}
    return poss_dict[command](row, col)
size = int(input())
race_number = input()
coordinate_list = []
race_distance = 0
e_t_row, e_t_col = 0, 0
p_row, p_col = 0, 0
matrix = []
finish = False
for row in range(size):
    temp_row = input().split(" ")
    matrix.append(temp_row)
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "T":
            coordinate_list.append([row, col])
coordinate_list = [x for l in coordinate_list for x in l]
e_t_row, e_t_col = coordinate_list[2], coordinate_list[3]

while True:
    passed_distance = 10
    command = input()
    if command == 'End':
        if matrix[p_row][p_col] != "F":
            print(f"Racing car {race_number} DNF.")
        break
    else:
        p_row, p_col = next_possition(p_row, p_col, command)
        if matrix[p_row][p_col] == "T":
            matrix[p_row][p_col] = "."
            p_row, p_col = e_t_row, e_t_col
            passed_distance = 30
        if matrix[p_row][p_col] == "F":
            race_distance += passed_distance
            finish = True
            break
    race_distance += passed_distance
    matrix[p_row][p_col] = "."
matrix[p_row][p_col] = "C"
if finish:
    print(f"Racing car {race_number} finished the stage!")
print(f"Distance covered {race_distance} km.")

for row in matrix:
    print(''.join(row))