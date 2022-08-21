unsorted_array = [5, 2, 4, 7, 1, 3, 2, 6]

a = unsorted_array

def bubble_sort():
    global a
    for i in range(len(a) - 2):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                temp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = temp


print("Unsorted Array is: ", unsorted_array)
bubble_sort()
print("Sorted Array is: ", a)