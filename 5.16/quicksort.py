
'''
快排是原地排序，不占用多余空间。因此不用return返回值，直接更改原队列
快速排序时间复杂度O(nlogn)
'''
def quicksort(array:list, l:int, r:int):
    if l < r:
        q = partition(array, l, r)
        quicksort(array, l, q - 1)
        quicksort(array, q + 1, r)


def partition(array:list, l:int, r:int):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1