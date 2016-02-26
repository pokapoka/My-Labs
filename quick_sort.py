def quicksort(alist): #worst case O(n^2)
    """return sorted [alist]"""
    quicksort_helper(alist,0,len(alist)-1)
    return alist

def quicksort_helper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)

        quicksort_helper(alist,first,splitpoint-1)
        quicksort_helper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark
