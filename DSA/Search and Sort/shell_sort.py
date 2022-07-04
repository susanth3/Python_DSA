"""
Shell Sort
Time complexity : O(n2) | Space complexity : O(1)
""" 

def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    
    while gap > 0:
        for i in range(gap,size):
            value = arr[i]
            j = i

            while j >= gap and value < arr[j-gap]:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = value
        gap = gap // 2
        
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
        shell_sort(elements)
        # print(f'sorted array: {elements}')
        print (shell_sort(elements))
