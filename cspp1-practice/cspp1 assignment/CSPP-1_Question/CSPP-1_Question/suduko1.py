# def getPossibilities(grid):
#      for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '.':
#                 r1 = getRow(grid, i)
#                 c1 = getCol(grid, j)
#                 grid = getSubgrid(grid, i, j)
#                 result = r1 + c1 + grid
#                 string = ''
#                 for k in result:
#                     # print("type.....",type(k))
#                     string += str(k)
#                     # print("type.....",type(k))
#                 print(string)

#             # if grid[i][j] == ".":
#             #     # print("fuck")
#             #     row = set(getRow(grid,j))
#             #     # print("rows",row)
#             #     column = set(getCol(grid,j))
#             #     # print("colums" , column)
#             #     subgrid = set(getSubgrid(grid,i,j))
#             #     # print("subgrid", subgrid)
#             #     # print("hello ",(row or column or subgrid))
#             #     # result = set(["1","2","3","4","5","6","7","8","9"]) -(row or column or subgrid)
#             #     # print("ful",result)
#             #     res = ""
#             #     for i in result:
#             #         res += i
                
# def getSubgrid(sudoku, val1, y):
#     g1 = []
#     # g2 = []
#     valid = False
#     for i in range(0,3):
#         for j in range(0,3):
#             if i == val1 and j == val2:
#                 valid = True
#             g1.append(sudoku[i][j])
#     if valid == True:
#         return g1

#     g1 = []
#     for i in range(0,3):
#         for j in range(3,6):
#             if i == val1 and j == val2:
#                 valid = True
#             g1.append(sudoku[i][j])
#     if valid == True:
#         return g1

#     g1 = []
#     for i in range(0,3):
#         for j in range(6,9):
#             if i == val1 and j == val2:
#                 valid = True
#             g1.append(sudoku[i][j])
#     if valid == True:
#         return g1

#     g1 = []
#     for i in range(3,6):
#         for j in range(0,3):
#             if i == val1 and j == val2:
#                 valid = True
#             g1.append(sudoku[i][j])
#     if valid == True:
#         return g1

#     g1 = []
#     for i in range(3,6):
#         for j in range(3,6):
#             if i == val1 and j == val2:
#                 valid = True
#             g1.append(sudoku[i][j])
#     if valid == True:
#         return g1

#     g1 = []
#     valid = False
#     for i in range(3,6):
#         for j in range(6,9):
#             if i == val1 and j == val2:
#                 valid = True
#             g1.append(sudoku[i][j])
#     if valid == True:
#         return g1

#     g1 = []
#     for i in range(6,9):
#         for j in range(0,3):
#             if i == val1 and j == val2:
#                 valid = True
#             g1.append(sudoku[i][j])
#     if valid == True:
#         return g1

#     g1 = []
#     for i in range(6,9):
#         for j in range(3,9):
#             if i == val1 and j == val2:
#                 valid = True
#             g1.append(sudoku[i][j])
#     if valid == True:
#         return g1

#     g1 = []
#     for i in range(6,9):
#         for j in range(6,9):
#             if i == val1 and j == val2:
#                 valid = True
#             g1.append(sudoku[i][j])
#     if valid == True:
#         return g1
    
# # def getSubgrid(grid,row, col):
# #     subgrid = []
# #     for i in range(row - (row%3),row-(2-(row%3))+1):
# #         for j in range(col - (col%3),col-(2-(col%3))+1):
# #             if grid[i][j] != ".":
# #                 subgrid.append(grid[i][j])
# #                 print("hello")
# #     print("degf...",subgrid)
# #     return subgrid                
# def validate(intput_1):
#     if len(intput_1) != 81:
#         raise Exception("Invalid Sudoku:Duplicate values")
#     elif "." not in intput_1:
#         raise Exception("Given sudoku is solved")
# def getRow(grid, row):
#     rows = []
#     for i in range(9):
#         if grid[row][i] != ".":
#             rows.append(i)
#     return rows
# def getCol(grid,col):
#     cols = []
#     for i in range(9):
#         if grid[i][col] != ".":
#             cols.append(i)
#     return cols
# def validateGrid(grid):
#     for i in range(9):
#         rows = getRow(grid,i)
#         cols = getCol(grid, i)
#         rowset = set(rows)
#         colset = set(cols)
#     if len(colset) != len(cols):
#         raise Exception("Invalid Sudoku:Duplicate values")
#     if len(rowset) != len(rows):
#         raise Exception("Invalid Sudoku:Duplicate values")

# def main():
#     intput_1 = input()
#     # print("#####",intput_1)
#     grid = []
#     k = 0
#     try:
#         for i in range(9):
#             row = []
#             for j in range(9):
#                 row.append(intput_1[k])
#                 # print("row........",row)
#                 k = k + 1
#             grid.append(row)
#         # print("sudoku...........",len(grid))
#         validate(intput_1)
#         validateGrid(grid)
#         getPossibilities(grid)
#     except Exception as e:
#         # raise e
#         print(e)
# if __name__ == "__main__":
#     main()
def getGrid(sudoku, x, y):
    g1 = []
    flag = False
    for i in range(0,3):
        for j in range(0,3):
            if i == x and j == y:
                flag = True
            g1.append(sudoku[i][j])
    if flag == True:
        return g1

    g1 = []
    for i in range(0,3):
        for j in range(3,6):
            if i == x and j == y:
                flag = True
            g1.append(sudoku[i][j])
    if flag == True:
        return g1

    g1 = []
    for i in range(0,3):
        for j in range(6,9):
            if i == x and j == y:
                flag = True
            g1.append(sudoku[i][j])
    if flag == True:
        return g1

    g1 = []
    for i in range(3,6):
        for j in range(0,3):
            if i == x and j == y:
                flag = True
            g1.append(sudoku[i][j])
    if flag == True:
        return g1

    g1 = []
    for i in range(3,6):
        for j in range(3,6):
            if i == x and j == y:
                flag = True
            g1.append(sudoku[i][j])
    if flag == True:
        return g1

    g1 = []
    flag = False
    for i in range(3,6):
        for j in range(6,9):
            if i == x and j == y:
                flag = True
            g1.append(sudoku[i][j])
    if flag == True:
        return g1

    g1 = []
    for i in range(6,9):
        for j in range(0,3):
            if i == x and j == y:
                flag = True
            g1.append(sudoku[i][j])
    if flag == True:
        return g1

    g1 = []
    for i in range(6,9):
        for j in range(3,9):
            if i == x and j == y:
                flag = True
            g1.append(sudoku[i][j])
    if flag == True:
        return g1

    g1 = []
    for i in range(6,9):
        for j in range(6,9):
            if i == x and j == y:
                flag = True
            g1.append(sudoku[i][j])
    if flag == True:
        return g1

def possibilities(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == '.':
                r1 = getRows(sudoku, i)
                c1 = getCols(sudoku, j)
                grid = getGrid(sudoku, i, j)
                rc = r1 + c1 + grid
                s = ''
                for k in range(1, 10):
                    if str(k) not in rc:
                        s += str(k)
                print(s)


def getCols(sudoku, val):
    clist = []
    for rlist in sudoku:
        if rlist[val] != '.':
            clist.append(rlist[val])
    return clist

def getRows(sudoku, val):
    rlist = []
    for i in sudoku[val]:
        if i != '.':
            rlist.append(i)
    return rlist

def validateSudoku(sudoku):
    for i in range(0,9):
        row = getRows(sudoku, i)
        col = getCols(sudoku, i)
        rdup = set(row)
        cdup = set(col)
        if len(row) != len(rdup):
            raise Exception("Invalid Sudoku:Duplicate values")
        if len(col) != len(cdup):
            raise Exception("Invalid Sudoku:Duplicate values")


def inputValidate(val):
    if len(val) != 81:
        raise Exception("Invalid input")
    elif '.' not in val:
        raise Exception("Given sudoku is solved")

def main():
    input1 = input()
    sudoku = []
    try:
        k = 0
        for i in range(9):
            row = []
            for j in range(0,9):
                row.append(input1[k])
                k = k + 1
            sudoku.append(row)
        inputValidate(input1)
        validateSudoku(sudoku)
        possibilities(sudoku)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    main()