def bubble_sort(arr):
    for i in range(len(arr) - 1, 1, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

testcase = [3,31,48,73,8,11,20,29,65,15]
print("Bubble Sort", bubble_sort(testcase))