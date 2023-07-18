def linear_search(list, target):
    #return the index postion
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None




def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list ")


numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 6)
verify(result)
'''
 Explanation: we created a function that accepts an array of items and loops through
 this function also accepts a target value which may or may not be included in the list
 it returns the index if its there we use the index inside the verify function 
'''
