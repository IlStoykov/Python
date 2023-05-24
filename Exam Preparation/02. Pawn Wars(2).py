def w_attak(w_row, w_col, b_row, b_col):
    b_list = [b_row, b_col]
    w_list = [[w_row - 1, w_col - 1], [w_row - 1, w_col + 1]]
    if b_list in w_list:
        return True

def b_attak(w_row, w_col, b_row, b_col):
    w_list = [w_row, w_col]
    b_list = [[b_row + 1, b_col - 1], [b_row - 1, b_col + 1]]
    if w_list in b_list:
        return True

def get_pole(row, col):
    v_dict = {0:'8', 1:'7', 2:'6', 3:'5', 4:'4', 5:'3', 6:'2', 7:'1'}
    h_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    return h_dict[col] + v_dict[row]

size = 8
next_row = 1
matrix = []
w_row, w_col = 0, 0
b_row, b_col = 0, 0
for row in range(size):
    temp_row = input().split(" ")
    for col in range(size):
        if temp_row[col] == "w":
            w_row, w_col = row, col
        elif temp_row[col] == "b":
            b_row, b_col = row, col
    matrix.append(temp_row)
while True:
    if w_attak(w_row, w_col, b_row, b_col):
        b_pos = get_pole(b_row, b_col)
        print(f"Game over! White win, capture on {b_pos}.")
        break
    else:
        if w_row == 0:
            w_pos = get_pole(w_row, w_col)
            print(f"Game over! White pawn is promoted to a queen at {w_pos}.")
            break
        w_row -= next_row

    if b_attak(w_row, w_col, b_row, b_col):
        w_pos = get_pole(w_row, w_col)
        print(f"Game over! Black win, capture on {w_pos}.")
        break
    else:
        if b_row == 7:
            b_pos = get_pole(b_row, b_col)
            print(f"Game over! Black pawn is promoted to a queen at {b_pos}.")
            break
        b_row += next_row