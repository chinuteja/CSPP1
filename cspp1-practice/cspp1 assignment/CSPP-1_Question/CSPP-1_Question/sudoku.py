def getrows(suduko, i):
    rowset = set()
    for k in range(0, 9):
        if suduko[i][k] != '.':
            rowset.add(suduko[i][k])
    return rowset
def getcols(suduko, j):
    colset = set()
    for k in range(0, 9):
        if(suduko[k][j] != '.'):
            colset.add(suduko[k][j])
    return colset            
def getgrid(suduko, i , j):
    gridset = set()
    for row in range(i - (i%3), i + (2 - i%3) + 1):
        for col in range(j - (j%3), j + (2 - j%3) + 1):
            if(suduko[row][col] != '.'):
                gridset.add(suduko[row][col])
    return gridset
def main():
    input_1 = input()
    if '.' not in input_1:
        print("Given Sudoko is solved")
    list1 = list(str(input_1))
    for i in range(len(list1)-1):
        if list1[i] == list1[i+9]:
            print("Invalid Sudoku:Duplicate values")
        i += 9

    else:
        suduko = []
        k = 0
        for i in range(0, 9):
            row = []
            for j in range(0,9):
                row.append(input_1[k])
                k = k + 1
            suduko.append(row)
        for row in range(0, 9):
           for col in range(0, 9):
               if(suduko[row][col] == '.'):
                result = set(['1','2','3','4','5','6','7','8','9']) - (getrows(suduko, row) | getcols(suduko, col) | getgrid(suduko, row, col))
                resultstr = ""
                for ele in result:
                    resultstr = resultstr + ele
                print(resultstr)           
if __name__ == '__main__':
    main()