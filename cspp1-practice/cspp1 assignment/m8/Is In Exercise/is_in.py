# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.
def is_found(low_value, high_value, char, sorted_str):
    mid_value = (low_value + high_value)//2
    print(mid_value)
    if sorted_str[mid_value] == char:
        return True
    elif mid_value == low_value or mid_value == high_value:
        return False
    else:
        if sorted_str[mid_value] < char:
            return is_found(mid_value,high_value,char,sorted_str)
        elif sorted_str[mid_value] > char:
            return is_found(mid_value,high_value,char,sorted_str)

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    sorted_str = sorted(aStr)
    sorted_str = ''.join(sorted_str)
    low_val = 0
    high_val = len(sorted_str)
    x = is_found(low_val, high_val, char, sorted_str)
    return x
def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))
if __name__== "__main__":
    main()