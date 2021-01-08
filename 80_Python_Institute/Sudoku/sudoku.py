#!/usr/bin/env python3


def get_sudoku():
    error = 0
    counter = 0
    sudoku_row = []
    sudoku_rows = []
    sudoku_columns = [[],[],[],[],[],[],[],[],[]]
    sudoku_squares = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0]]

    while counter < 9:
        sudoku_row = []
        row = input(f"Input the row {counter} of the sudoku: ")
        try:
            for index, value in enumerate(row):
                sudoku_row.append(int(value))
                sudoku_columns[index].append(int(value))
            error = 0
        except ValueError:
            print("Only integers are allowed, please try again")
            error = 1
        if error == 1:
            continue
        sudoku_rows.append(sudoku_row)
        counter += 1
    #Form Squares
#    print(sudoku_rows)
#    print(sudoku_columns)
    for i in range(9):
        for k in range(3):
            if i < 3:
                sudoku_squares[i][k*3:(k+1)*3:1] = sudoku_rows[k][i*3:(i+1)*3:1]
            if i >= 3 and i < 6:
                sudoku_squares[i][k*3:(k+1)*3:1] = sudoku_rows[k][(i-3)*3:(i-2)*3:1]
            if i >= 6 and i < 9:
                sudoku_squares[i][k*3:(k+1)*3:1] = sudoku_rows[k][(i-6)*3:(i-5)*3:1]
# Debug Lines 
#    print(sudoku_squares)
    return [sudoku_rows, sudoku_columns, sudoku_squares];

def test_sudoku(sudoku_rows, sudoku_columns, sudoku_squares):
    # row testing first
    error = 0
    for row in sudoku_rows:
        if len(row) > len(set(row)):
            print(f"Error found in row: {row} ; sudoku is not correct")
            error = 1
            break
    for column in sudoku_columns:
        if len(column) > len(set(column)):
            print(f"Error found in column: {column} ; sudoku is not correct")
            error = 1
            break
    for square in sudoku_squares:
        if len(square) > len(set(square)):
            print(f"Error found in square: {square} ; sudoku is not correct")
            error = 1
            break
    if error == 1:
        print("GAME OVER")
    else:
        print("Congratulations the sudoku is correct!!")


def main():
    sudoku_rows, sudoku_columns, sudoku_squares = get_sudoku()
    test_sudoku(sudoku_rows, sudoku_columns, sudoku_squares)


if __name__ == "__main__":
    main()
