# Array Problems

# Anagram


def anagram(s1, s2):

    s1 = list(s1.replace(' ', '').lower())
    s2 = list(s2.replace(' ', '').lower())

    s1.sort()
    s2.sort()

    return s1 == s2


def anagram2(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


# Using Dictionaries/Hash Tables
def anagram3(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge Case check
    if len(s1) != len(s2):
        return False

    count = {}  # Dictionary

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True
#-------------------------------------------------#

# Pair Sum
# Not Optimal


def TwoSum(numbers, target):
    for i, j in enumerate(numbers):
        for x, y in enumerate(numbers):
            if j + y == target and i != x:
                return (i, j)

# Optimal


def pair_sum(arr, k):

    if len(arr) < 2:
        return 'Less than 2 numbers'

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))

    print '\n'.join(map(str, list(output)))
#-------------------------------------------------#

# Find Missing number
# O(NlogN). But can be done in O(N)


def finder(arr1, arr2):

    arr1.sort()
    arr2.sort()

    # Tuple
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

# O(N) Solution


def finder2(arr1, arr2):
    # Same as any dictionary but if key doesn't exist, adds key without error
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

# Even better


def finder3(arr1, arr2):
    result = 0

    # Perform XOR between the numbers in the arrays
    for num in arr1 + arr2:  # Concatinate array 1 and array 2
        result ^= num
        print result

    return result

# -------------------------------------------------#

# Largest continuous Sum


def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

# -------------------------------------------------#

# Sentance Reversal


def rev_word(s):
    print(' '.join(s.split()[::-1]))

# To do it manually:


def rev_word2(s):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] != ' ':

                # Get index where word ends either by space or by end of line
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1

    # Join the reversed words
    return reversal(words)


def reversal(lst):
    temp = []

    while lst:
        temp.append(lst.pop())

    print(' '.join(temp))

# -------------------------------------------------#


# String Compression

def compress(s):

    r = ""
    length = len(s)

    if length == 0:
        return ""

    if length == 1:
        return s + "1"

    cnt = 1
    i = 1

    while i < length:
        if s[i] == s[i - 1]:
            cnt += 1

        else:
            r = r + s[i - 1] + str(cnt)

        i += 1

    r = r + s[i - 1] + str(cnt)

    return r

# -------------------------------------------------#

# Unique Characters in String


def uni_char(s):
    return len(set(s)) == len(s)


def uni_char2(s):
    temp = ""
    for letter in s.lower():
        if letter not in temp:
            temp += letter
        else:
            return False
    return True

# -------------------------------------------------#
