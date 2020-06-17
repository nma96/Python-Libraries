# For unordered list


def sequentialSearch(arr, ele):

    position = 0
    found = False

    while position < len(arr) and not found:

        if arr[position] == ele:
            found = True

        else:
            position += 1

    return found


# For ordered


def orderedSequentialSearch(arr, ele):

    position = 0
    found = False
    stopped = False

    while position < len(arr) and not found and not stopped:

        if arr[position] == ele:
            found = True

        else:
            if arr[position] > ele:
                stopped = True

            else:
                position += 1

    return found
