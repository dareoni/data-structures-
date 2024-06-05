# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break
    return arr

# Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Original list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sort the list using each algorithm
sorted_list_bubble = bubble_sort(original_list.copy())
sorted_list_selection = selection_sort(original_list.copy())
sorted_list_insertion = insertion_sort(original_list.copy())

# Print the results
print("Original List:", original_list)
print("Sorted List (Bubble Sort):", sorted_list_bubble)
print("Sorted List (Selection Sort):", sorted_list_selection)
print("Sorted List (Insertion Sort):", sorted_list_insertion)
