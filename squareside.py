"""
Main module
githab repo:
https://github.com/ivddorrka/lab1.3.git
"""
import math

rules1 = "If you want to enter a number like: √5, then write it this way: sqrt(5)"
rules2 = "First and second sides should be equal"
rules3 = "If your number is deciminal write it next way: 4.4 (using dot, not a coma)"

print(rules1)
print(rules2)
print(rules3)

def checking_func(a_side):
    """To convert length of a side to float and check whether 
    there's are roots
    >>> checking_func('2sqrt(4)')
    4.0
    """
    if len(a_side.split('(')) == 2:
        sq_num = list((a_side.split('('))[1])
        del sq_num[-1]
        sq_num1 = ''.join(sq_num)
        if len(a_side.split('*')) == 2:
            first_num = a_side.split('*')[0]
            res_num = round(float(first_num) * math.sqrt(float(sq_num1)), 2)
            return res_num
        elif (a_side.split('s')[0]) != '':
            try:
                number_here = float(a_side.split('s')[0])
                return number_here * math.sqrt(float(sq_num1))
            except ValueError:
                print("Try again")
                return 'wrong number'
        else:
            return math.sqrt(float(sq_num1))
    else:
        return float(a_side)

# print(checking_func('2'))

def user_input():
    """To get data from user"""
    a_side = input("Enter the first side of yout triangular: ")
    b_side = input("Enter the second side of yout triangular, should be equalt to the first one: ")
    c_side = input("Enter the third side of yout triangular: ")
    acc_count = input("Enter the length to look up to: ")
    a1_side = checking_func(a_side)
    b1_side = checking_func(b_side)
    c1_side = checking_func(c_side)
    acc1_count = checking_func(acc_count)
    return a1_side, b1_side, c1_side, acc1_count

def height(b_side, c_side):
    """Function to find the heigt to the third side
    >>> height(10, 12)
    8.0
    """
    bh = math.sqrt(b_side**2 - (0.5 * c_side)**2)
    return round(bh, 2)
# print(height(10, 12))

def find_km(b_side, c_side):
    """Function to find the length of the square
    >>> find_km(10, 12)
    4.8
    """
    bh = height(b_side, c_side)
    var1 = 0.5 * c_side * bh
    var2 = bh + c_side
    square_side = 2 * (var1 / var2)
    return round(square_side, 2)
# print(find_km(10, 12))

def find_side(a_side, b_side, c_side, acc_count):
    """Main function to count the side of a square
    >>> find_side(10, 10, 12, 64.77)
    310.896
    """
    square_side = find_km(b_side, c_side)
    likti = round(acc_count * square_side, 3)
    return likti
# print(find_side(10, 10, 12, 64.77))

def into_file():
    """Writes into file"""
    user_data = user_input()
    a_side = user_data[0]
    b_side = user_data[1]
    c_side = user_data[2]
    acc_count = user_data[3]
    side = find_side(a_side, b_side, c_side, acc_count)
    if a_side != b_side:
        print("Should be equal!!!")
        return into_file()
   
    file_here = open('Results.txt', 'a')
    file_here.write('The length of a side of a square: ' + '{}'.format(side) + '\n')
    file_here.close
    return file_here
# print(into_file())

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()