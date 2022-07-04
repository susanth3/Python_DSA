
"""
Cycle Sort
Time complexity : O(n2) | Space complexity : O(1)
""" 

def cycle_Sort(array):
    
    size = len(array)
    i = 0

    while i < size:
        if array[i] != i+1 :
            new_index = array[i] - 1
            temp = array[i]
            array[i] = array[new_index]
            array[new_index] = temp
        else:
            i += 1

# driver code
array = [1,2,3,4,5,8,9,7,6]
print("The original array is:", array)
n = len(array)
cycle_Sort(array)
print("The sorted array is: ",array)
