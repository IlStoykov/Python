size = 6
p1, p2 = [str(x) for x in input().split(", ")]
p1_rest = False
p2_rest = False
matrix = []
for row in range(size):
    temp_row = list(input().split(" "))
    matrix.append(temp_row)
while True:
    p1_coordinates = input()
    if not p1_rest:
        p1_row, p1_col = map(int, p1_coordinates.strip("(").strip(")").split(", "))
        if matrix[p1_row][p1_col] == "E":
            print(f"{p1} found the Exit and wins the game!")
            break
        if matrix[p1_row][p1_col] == "T":
            print(f"{p1} is out of the game! The winner is {p2}.")
            break
        if matrix[p1_row][p1_col] == "W":
            print(f"{p1} hits a wall and needs to rest.")
            p1_rest = True
    else:
         p1_rest = False

    p2_coordinates = input()
    if not p2_rest:
        p2_row, p2_col = map(int, p2_coordinates.strip("(").strip(")").split(", "))
        if matrix[p2_row][p2_col] == "E":
            print(f"{p2} found the Exit and wins the game!")
            break
        if matrix[p2_row][p2_col] == "T":
            print(f"{p2} is out of the game! The winner is {p1}.")
            break
        if matrix[p2_row][p2_col] == "W":
            print(f"{p2} hits a wall and needs to rest.")
            p2_rest = True
    else:
        p2_rest = False







