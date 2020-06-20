'''
    Problem Statement: Given a sentance, return it be decreasing the $ values by 10%

    Ex 1: 
        Input: Alice spent $10.00 this week and $12.00 the next week
        Output: Alice spent $9.00 this week and $10.80 the next week

    Ex 2: 
        Input: Alice spent $10.000 this week and $12.00 the next week
        Output: Alice spent $10.000 this week and $10.80 the next week

    Ex 3: 
        Input: Alice spent $10.0 this week and $12.00 the next week
        Output: Alice spent $10.0 this week and $10.80 the next week

    Notice in examples 2 and 3, the first value is not converted as it does not follow a pattern

    Constraints:
    The value must follow the pattern: <currency><any number of digits><.><digit><digit>


    Follow Up: Implement for any currency (Not just $)
'''


import re


def PatternMatch(String):

    # RegEx: Find literal [$] followed by 1 or more digits [0-9](+) 
        # followed by literal [.] followed by 2 digits (\d{2}) and word break(\b)
    pattern = re.compile(r'[$][0-9]+[.]\d{2}\b')
    # Above regular expression finds all the dollar values. 
    # To add compatibility to other currencies, add those currencies
        # to the first bracket in the below expression


    # finditer finds all the occurances of the RegEx and 
    matches = pattern.finditer(String)

    # Values list will store indexes of all the matched values as a (start, end) tupple
    values = []
    for match in matches:
        values.append((match.start()+1, match.end()))

    # Edge case check if there are no values that match
    if values == [] or values is None:
        return String

    # Creating a copy of the string which will be returned with new values
    result = String

    # The below for loop is replacing those values with the reduced values
    for value in values:
        before = String[value[0]:value[1]]
        after = reduceBy10(float(String[value[0]:value[1]]))
        
        result = result.replace(before, after)

    return result

def reduceBy10(number):
    # Perform the 10% deduction and return the number with exactly 2 digits after the decimal point
    return '%.2f' % float(number*0.9)


def main():
    inputText = input("Enter the String: ")
    print("String after Reduction: " + PatternMatch(inputText))

if __name__ == '__main__':
    main()