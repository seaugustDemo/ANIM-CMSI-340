# getMaxParm.py
#
# Change history:
#   15-MAR-2015  S.E. August   .Resolved naming conflict with another version of
#                                getMaxParm.py, to use val1, val2 in place of number1,
#                                number 1.

# Return the max of two numbers
def max(num1, num2):
    """Returns the larger of num1 and num2"""
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result

def main(num1, num2):
    i = num1
    j = num2
    k = max(i, j)  # Call the max function
    print("The larger number of", i, "and", j, "is", k)

# Initialize variables
val1 = 8
val2 = 3

# Run the program
main(val1, val2)   # Call the main function

