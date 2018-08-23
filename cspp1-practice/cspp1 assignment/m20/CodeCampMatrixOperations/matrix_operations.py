'''
author : teja
date : 23/8/2018
'''
def mult_matrix(m_1, m_2, c_1, r_2, r_1):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if c_1 == r_2:
        multiplication_matrix = []
        for i in range(r_1):
            temp = []
            for j in range(r_1):
                sum_val = 0
                for k in range(c_1):
                    sum_val = sum_val + (m_1[i][k] * m_2[k][j])
                temp.append(sum_val)
            multiplication_matrix.append(temp)
        return multiplication_matrix
    else:
        print("Error: Matrix shapes invalid for mult")
        return None
   
def add_matrix(m_1, m_2, r_1, r_2, c_1, c_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if r_1 == r_2 and c_1 == c_2:
        add_matrix = []
        for i in range(len(m_1)):
            temp = []
            for j in range(len(m_1[0])):
                temp.append(m_1[i][j]+m_2[i][j])
            add_matrix.append(temp)
        return add_matrix
    else:
        print("Error: Matrix shapes invalid for addition")
    return None
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    dimensions = input().split(",")
    r_1 = int(dimensions[0])
    c_1 = int(dimensions[1])
    m_1 = []
    for i in range(0,r_1):
        m_1.append(list(map(int, input().split())))
    return r_1, c_1, m_1

def main():
    # read matrix 1
    (m_1, r_1, c_1) = read_matrix()
    (m_2, r_2, c_2) = read_matrix()
    print(add_matrix(m_1, m_2, r_1, c_1, r_2, c_2))
    print(mult_matrix(m_1, m_2, r_1, c_1, r_2))    

if __name__ == '__main__':
    main()
