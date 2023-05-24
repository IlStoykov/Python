from collections import deque
def next_possition(row, col,command):
    poss_dict = {"right":lambda r, c:[r, c + 1], "left":lambda r, c:[r, c - 1],
                 "up":lambda r, c:[r -1, c], "down":lambda r, c:[r + 1, c]}
    return poss_dict[command](row, col)

def in_side(row, col, size):
    return 0 <= row < size and 0 <= col < size

size = int(input())
commands = deque(input().split(", "))
matrix = []
haz_collected = 0
s_row, s_col = 0, 0
cycle_stop = False
for row in range(size):
    t_row = list(input())
    for col in range(size):
        if t_row[col] == "s":
            s_row = row
            s_col = col
    matrix.append(t_row)
matrix[s_row][s_col] = "*"
while commands:
    command = commands.popleft()
    s_row, s_col = next_possition(s_row, s_col, command)

    if not in_side(s_row, s_col, size):
        print("The squirrel is out of the field.")
        cycle_stop = True
        break
    if matrix[s_row][s_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        cycle_stop = True
        break

    if matrix[s_row][s_col] == "h":
        haz_collected += 1
        matrix[s_row][s_col] = "*"

    if haz_collected == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if haz_collected < 3 and not cycle_stop:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {haz_collected}")