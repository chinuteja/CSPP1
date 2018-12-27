def getRowset(grid,row):
    rowset = set()
    for i in range(9):
        if grid[row][i] != ".":
            # print("..........",grid[row][i])
            rowset.add(grid[row][i])
            # print("fuck ............",rowset)
            # print(rowset)
    return rowset
def rowCheck(grid):
    for i in range(8):
        row = grid[i]
        k = 0
        for j in range(8):
            if row[k] == row[j]:
                raise Exception ("Invalid Sudoku:Duplicate values")
            k = k + 1
def getColset(grid,col):
    colset = set()
    for j in range(9):
        if grid[j][col] != ".":
            colset.add(grid[j][col])
            # print("dsafjfhkajfha",colset)
    return colset
def getSubgrid(grid,row, col):
    subgrid = set()
    for i in range(row - (row%3),row-(2-(row%3))+1):
        for j in range(col - (col%3),col-(2-(col%3))+1):
            if grid[i][j] != ".":
                subgrid.add(grid[i][j])
    return subgrid
def main():
    input_1 = input()
    # print("length of input" , len(input_1))
    # 
    if "." not in input_1:
        print("Given sudoku is solved")
    elif (len(input_1) != 81):
        print("Invalid input")
    # elif (len(input_1) == 81):
    #     flag = False
    #     for i in range(len(input_1)):
    #         for j in range(9):
    #             if input_1[i] == input_1[j]:
    #                 flag = True
    #     if flag == True:
    #         print("Invalid Sudoku:Duplicate values")

    else:
        grid = []
        k = 0
        for i in range(9):
            row = []
            for j in range(9):
                row.append(input_1[k])
                k = k + 1
            grid.append(row)
        try:
            rowCheck(grid)
            for row in range(9):
                for col in range(9):
                    if (grid[row][col]) == ".":
                        result = set(['1','2','3','4','5','6',"7",'8','9']) - (getRowset(grid,row) or getColset(grid,col) or getSubgrid(grid,row,col))
                        result_1 = ""
                        # print(result)
                        for x in result:
                            result_1 += x
                            print(result_1)

        except Exception as e:
            raise e
        
                    
if __name__ == "__main__":
    main()
