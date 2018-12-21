def check_suduko(suduko):
    count = 0
    for row in suduko:
        # print(row)
        for i in row:
            if i == ".":
                count = count + 1
                
            
    if count == 0:
        return "Given sudoku is solved"
def main():
    suduko = []
    input_1 = str(input())
    i = 0
    j = 0
    while i< len(input_1):
        suduko.insert(j,list((input_1[i:i+9])))
        # print("sujo",suduko)
        i = i + 9
        j = j + 1
    print(check_suduko(suduko))
    # print(suduko)
if __name__ == "__main__":
    main()
