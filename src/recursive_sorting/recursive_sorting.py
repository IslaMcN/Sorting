# TO-DO: complete the helpe function below to merge 2 sorted arrays
# from heapq import merge as Merge

# def merge( arrA, arrB ):
#     return list(Merge(arrA, arr2)
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j< len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j< len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
# Maintain two pointers which point to start of the segments which have to 
# be merged.
    start2 = mid + 1
    if(arr[mid] <= arr[start2]):
        return
# Compare the elements at which the pointers are present.
    while (start <= mid and start2 <= end):
        if(arr[start] <= arr[start2]):
            start += 1
# If element1 < element2 then element1 is at right position, simply increase 
# pointer1.
        else:
            value = arr[start2]
            index = start2
            while (index != start):
                arr[index] = arr[index -1]
                index -= 1
# Else place element2 in its right position and all the elements at the 
# right of element2 will be shifted right by one position. Increment all the 
# pointers by 1.
            arr[start] = value
            start += 1
            mid += 1
            start += 1
            print(arr)
            return arr

my_list = [10, 20, 22, 5]

##Only works so far with my list since it is smaller than the ones in the test.



def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if (l < r):
        m = 1 + (r-1) //2
        merge_sort_in_place(arr, 1, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m , r)

    return arr
merge_sort_in_place(my_list, 0, len(my_list)-1)

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
