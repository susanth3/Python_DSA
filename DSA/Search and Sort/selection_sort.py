"""
Selection Sort
Time complexity : O(n2) | Space complexity : O(1)
""" 

def swap(a,b,arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def selection_sort(arr):
    size = len(arr)
    
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            swap(i,min_index,arr)


if __name__ == '__main__':

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        ["mona", "dhaval", "aamir", "tina", "chang"],
        [6]
    ]

    for elements in tests:
        selection_sort(elements)
        print(f'sorted array: {elements}')