"""
Quick Sort
Time complexity : O(n2) | Space complexity : O(log n)
""" 

def swap(a,b,arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def quick_sort(arr,start,end):
    if start < end :
        position = partition(arr,start,end)
        quick_sort(arr,start,position-1)
        quick_sort(arr,position+1,end)

def partition(arr,start,end):
    pivot_position = start
    pivot = arr[pivot_position]

    while start < end:

        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            swap(start,end,arr)

    swap(pivot_position,end,arr)

    return end

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
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
