

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    print(arr)
    n = len(arr)
    # loop through n-1 elements
    for i in range(n-1,0,-1):
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        max = 0
        for j in range(1, i+1):
            if arr[j] > arr[max]:
                max = j
        temp = arr[i]
        arr[i] = arr[max]
        arr[max] = temp
            
               



        




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: 
                 arr[j], arr[j+1]= arr[j+1], arr[j]
        #i needs to be in zero index
        #i[0]
    
        ##arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
    
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1):
    counts = [0] * (maximum + 1)
    for item in arr:
        counts[item] += 1
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count
    sorted_list = [None] * len(arr)
    for item in arr:
        sorted_list[ counts[item] ] = item
        counts[item] += 1

    return sorted_list

    