def is_difference(w_col, b_col):
    return abs(w_col - b_col) > 1

def find_winner(w_row, w_col, b_row, b_col):
    b_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
    w_list = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
    w_steps = 7 - (7-w_row)
    b_steps = 7 - b_row
    if w_steps - b_steps <= 0:
        return f"Game over! White pawn is promoted to a queen at {w_list[w_col]}."
    else:
        return f"Game over! Black pawn is promoted to a queen at {b_list[b_col]}."

def white_check(w_row, w_col, b_row, b_col):
    check_list = [[w_row-1, w_col-1], [w_row-1, w_col+1]]
    if [b_row, b_col] in check_list:
        return True
def get_pole(b_row, b_col):
    v_dict = {0:'8', 1:'7', 2:'6', 3:'5', 4:'4', 5:'3', 6:'2', 7:'1'}
    h_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    return h_dict[b_col] + v_dict[b_row]

def black_check(w_row, w_col, b_row, b_col):
    check_list = [[b_row+1, b_col-1], [b_row+1, b_col+1]]
    if [w_row, w_col] in check_list:
        return True

matrix = []
w_row, w_col = 0, 0
b_row, b_col = 0, 0
for row in range(8):
    temp_row = input().split()
    for col in range(8):
        if temp_row[col] == "w":
            w_row, w_col = row, col
        elif temp_row[col] == "b":
            b_row, b_col = row, col
    matrix.append(temp_row)

if is_difference(w_col, b_col):
    print(find_winner(w_row, w_col, b_row, b_col))
else:
    while True:
        if white_check(w_row, w_col, b_row, b_col):
            pole = get_pole(b_row, b_col)
            print(f"Game over! White win, capture on {pole}.")
            break
        else:
            w_row -= 1

        if black_check(w_row, w_col, b_row, b_col):
            pole = get_pole(w_row, w_col)
            print(f"Game over! Black win, capture on {pole}.")
            break
        else:
            b_row += 1