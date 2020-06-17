# Balanced Parenthesis Check

# My Solution (Doesn't use Stacks)
# Works for ][ but should not.


def balance_check(s):

    count1 = 0
    count2 = 0
    count3 = 0
    # Edge case for odd number of parenthesis
    if len(s) % 2 != 0:
        return False

    for openB in s:
        if openB == '(':
            count1 += 1
        if openB == '[':
            count2 += 1
        if openB == '{':
            count3 += 1

    for closeB in s:
        if closeB == ')':
            count1 -= 1
        if closeB == ']':
            count2 -= 1
        if closeB == '}':
            count3 -= 1

    return count1 == count2 == count3 == 0


# Stack Solution (Better)

def balance_check2(s):

    if len(s) % 2 != 0:
        return False

    # Create a set of opening brackets {'(', '[', '{'}
    opening = set('([{')

    # Create a set of tuples that are Matching Parenthesis
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    # Create an empty Stack
    stack = []

    for paren in s:
        # Push an opening parenthesis into the stack
        if paren in opening:
            stack.append(paren)

        # The parenthesis is not an opening one. So either EOF or Closing Parenthesis
        else:
            # If EOF, return False as no matching closing parenthesis found after EOF
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            # If Closing parenthesis, check if last_open and paren are matching.
            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0

# -------------------------------------------------#

# Implement Queue using 2 Stacks


class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):

        self.stack1.append(element)

    def dequeue(self):
        # Check if stack2 is not empty
        if not self.stack2:

            # until stack1 is empty, pop from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # pop stack2
        return self.stack2.pop()

# -------------------------------------------------#
