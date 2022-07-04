"""
Insertion Sort
Time complexity : O(n2) | Space complexity : O(1)
""" 

def insertion_sort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        j = i-1
        while j >= 0 and value < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value
    return arr


if __name__ == '__main__':
    
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        # print(f'sorted array: {elements}')
        print (insertion_sort(elements))
