# Version 1: Iterative


def BinarySearch(arr, ele):
    '''
    Arr has to be sorted
    '''

    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) / 2

        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1


# Version 2: Recursive


def BinarySearch2(arr, ele):

    # Base Case
    if len(arr) == 0:
        return False

    else:

        mid = len(arr) / 2

        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return BinarySearch2(arr[:mid], ele)
            else:
                return BinarySearch2(arr[mid + 1:], ele)
