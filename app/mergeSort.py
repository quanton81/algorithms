import sys

unsorted_array = [5, 2, 4, 7, 1, 3, 2, 6]

a = unsorted_array

def merge(p, q, r):
    global a
    n1 = q - p + 1
    n2 = r - q
    li = [int] * (n1 + 1)
    ri = [int] * (n2 + 1)
    li[n1] = sys.maxsize
    ri[n2] = sys.maxsize
    for i in range(n1):
        li[i] = a[p + i - 1]
    for j in range(n2):
        ri[j] = a[q + j]
    i = j = 0
    for k in range(p - 1, r):
        if len(li) >= i + 1 and len(ri) >= j + 1 and li[i] < ri[j]:
            a[k] = li[i]
            i = i + 1
        else:
            a[k] = ri[j]
            j = j + 1

def merge_sort(p, r):
    global a
    if p < r:
        q = int((p + r) / 2)
        merge_sort(p, q)
        merge_sort(q + 1, r)
        merge(p, q, r)

print("Unsorted Array is: ", unsorted_array)
merge_sort(1, len(a))
print("Sorted Array is: ", a)