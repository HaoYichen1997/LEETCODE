
'''
二分法查找 时间复杂度O(logn)
'''
def binary_search(array:list, b: int, e:int, g): #b begin e end g goal
    if len(array) == 0:
        return -1

    mid = (b + e) // 2
    if array[mid] == g:
        return mid
    elif array[mid] > g:
        return binary_search(array, b, mid-1, g)
    elif array[mid] < g:
        return binary_search(array, mid+1, e, g)
