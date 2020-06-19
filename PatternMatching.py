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

inputText = '''Alice spent $10.00 this week and $12.00 the next week'''

# RegEx: Find literal [$] followed by 1 or more digits [0-9](+) 
    # followed by literal [.] followed by 2 digits (\d{2}) and word break(\b)
pattern = re.compile(r'[$][0-9]+[.]\d{2}\b')
# Above regular expression finds all the dollar values. 
# To add compatibility to other currencies, add those currencies
    # to the first bracket in the below expression

matches = pattern.finditer(inputText)

for match in matches:
    print(match)

