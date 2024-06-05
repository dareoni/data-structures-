def find_min_max_recursive(sequence, start_idx=0, end_idx=None):
    if end_idx is None:
        end_idx = len(sequence) - 1

    if start_idx == end_idx:
        return sequence[start_idx], sequence[start_idx]

    if start_idx == end_idx - 1:
        return (sequence[start_idx], sequence[end_idx]) if sequence[start_idx] < sequence[end_idx] else (sequence[end_idx], sequence[start_idx])

    mid_idx = (start_idx + end_idx) // 2

    left_min, left_max = find_min_max_recursive(sequence, start_idx, mid_idx)
    right_min, right_max = find_min_max_recursive(sequence, mid_idx + 1, end_idx)

    return min(left_min, right_min), max(left_max, right_max)

# Test the function
sequence = [3, 7, 2, 9, 1, 5, 4]
min_val, max_val = find_min_max_recursive(sequence)
print("Minimum value:", min_val)
print("Maximum value:", max_val)

def reverse_list_recursive(lst):

    if len(lst) <= 1:
        return lst

    return reverse_list_recursive(lst[1:]) + [lst[0]]

# Test the function
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list_recursive(original_list)
print("Original list:", original_list)
print("Reversed list:", reversed_list)