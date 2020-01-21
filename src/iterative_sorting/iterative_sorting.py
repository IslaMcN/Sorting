n = len(arr) - 1

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, n):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        if i < n:
            j = i + 1
            if j < n:
                if arr[j] < arr[smallest_index]:
                    smallest_index = j
                    for j in range(0, n):
                        j + 1
            # TO-DO: swap
            else:
                arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
                return i + 1



        




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    have_swapped = True
        #i needs to be in zero index
        #i[0]
        while have_swapped:
            have_swapped = False
        #Compare to right hand neighbor
        #i[0 + 1]
        for i in range(0, n):

        #If i[0+1] < i[0]:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        ##arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
    
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr