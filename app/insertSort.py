unsorted_array = [5,2,4,6,1,3]

def insert_sort(array_of_integers):
    for j in range(len(array_of_integers)):
        if j < 1:
            continue
        key = array_of_integers[j]
        i = j - 1
        while i >= 0 and array_of_integers[i] > key:
            array_of_integers[i + 1] = array_of_integers[i]
            i = i - 1
        array_of_integers[i + 1] = key

    return array_of_integers

print("Unsorted Array is: ", unsorted_array)
sorted_array = insert_sort(unsorted_array)
print("Sorted Array is: ", sorted_array)