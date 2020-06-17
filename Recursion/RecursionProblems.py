# Cumulative sum of 0 to n


def rec_sum(n):

    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)

# -------------------------------------------------#

# Sum of all the individual digits in that integer
# 4321 => 4+3+2+1


def sum_func(n):
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_func(n // 10)

# -------------------------------------------------#

# Split words from sentence only if the word exists in dictionary


def word_split(phrase, list_of_words, output=None):

    # Since this is a recursive function, each time output will be made to None
    if output is None:
        output = []  # Terminating Criteria

    # For each word in list of words
    for word in list_of_words:

        # If phrase begins with the word, add word to output
        if phrase.startswith(word):

            output.append(word)

            # Recursuvely call function but after splicing the word out
            return word_split(phrase[len(word):], list_of_words, output)

    # When all words have been traversed, return the output
    return output

# word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
# Output ==> ['i', 'love', 'dogs', 'John']
# word_split('themanran',['clown','ran','man'])
# Output ==> []

# -------------------------------------------------#

# Reverse a string


def reverse(s):

    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]

# -------------------------------------------------#

# String Permutation


def permute(s):

    output = []

    # Base Case
    if len(s) == 1:
        output = [s]

    #  Recursion
    else:

        for i, letter in enumerate(s):
            for perm in permute(s[:i] + s[i + 1]):
                output += [letter + perm]

    return output

# -------------------------------------------------#

# Fibonacci using Iteration, recursion and memoization


def fib_iterative(n):

    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b
    return a


def fib_recursion(n):
    if n == 0 or n == 1:
        return n

    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_memoization(n):

    # Base Check
    if n == 0 or n == 1:
        return n

    # Check Cache
    if cache[n] is not None:
        return cache[n]

    # Keep setting cache
    cache[n] = fib_memoization(n - 1) + fib_memoization(n - 2)

    return cache[n]

# -------------------------------------------------#


# Coin Change Problem: Minimum number of coins to reach target (using the coins allowed)
# Not the best solution in terms of time (takes too much time when number is weird)

def rec_coin(target, coins):

    min_coins = target

    # Base Case
    if target in coins:
        return 1

    else:

        # For every coin value <= target
        for i in [c for c in coins if c <= target]:

            # Add coin count + recursively call function for target-i
            num_coins = 1 + rec_coin(target - i, coins)

            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


# Better solution in terms of time but not so much in terms of space

def rec_coin_dynam(target, coins, known_results):
    '''
    INPUT: This funciton takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)

    OUTPUT: Minimum number of coins needed to make the target.
    '''

    # Default output to target
    min_coins = target

    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1

    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]

    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynam(target - i, coins, known_results)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins

                # Reset the known result
                known_results[target] = min_coins

    return min_coins

# -------------------------------------------------#
