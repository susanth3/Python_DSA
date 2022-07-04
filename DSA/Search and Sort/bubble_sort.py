"""
Bubble sort
Time complexity : O(n2) | Space complexity : O(1)
""" 

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def bubble_sort(arr):
    size = len(arr)
    for i in range(size-1):
        swapping = False
        for j in range(size-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = swap(arr[j],arr[j+1])
                swapping = True
        if swapping != True:
            break
        

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    # elements = [1,2,3,4,2]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    bubble_sort(elements)
    print (elements)