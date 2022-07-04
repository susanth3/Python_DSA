"""
Linear Search
Time complexity : O(n) | Space complexity : O(1)
""" 
def linear_search(arr,tar):
    for index,element in enumerate(arr):
        if element == tar:
            return index
    return -1

"""
Binary Search (Iterative)
Time complexity : O(log n) | Space complexity : O(1)
""" 
def binary_search(arr,tar):
    size = len(arr)-1
    left = 0
    right = size

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            left = mid + 1
        else:
            right = mid -1
            
    return -1

"""
Binary Search (Recursive)
Time complexity : O(log n) | Space complexity : O(1)
""" 
def binary_search_rec(arr,left,right,tar):

    if left <= right:
        mid = (left + right) // 2

        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            return binary_search_rec(arr,mid+1,right,tar)
        else:
            return binary_search_rec(arr,left,mid-1,tar)

    return -1


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")

    index = binary_search_rec(numbers_list, 0, len(numbers_list)-1 , number_to_find)
    print(f"Number found at index {index} using binary search_recursive method")   
