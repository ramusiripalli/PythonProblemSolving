def find_largest_iterative(arr):
    """
    Iterative approach to find the largest element in an array.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Handle empty array case
    if not arr:
        return None
    
    # Initialize max with first element
    max_element = arr[0]
    
    # Iterate through the array starting from second element
    for num in arr[1:]:
        # Update max_element if current number is greater
        if num > max_element:
            max_element = num
    
    return max_element

# ---------------------------------------------------------------------------------------------------

def find_largest_builtin(arr):
    """
    Using Python's built-in max() function.
    Time Complexity: O(n) (internally it's the same as iterative)
    Space Complexity: O(1)
    """
    # Handle empty array case
    if not arr:
        return None
    
    return max(arr)


#---------------------------------------------------------------------------------------

def find_largest_sorting(arr):
    """
    Find largest by sorting the array.
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for timsort (Python's sorting algorithm)
    """
    # Handle empty array case
    if not arr:
        return None
    
    # Sort the array in ascending order
    sorted_arr = sorted(arr)
    
    # Last element will be the largest
    return sorted_arr[-1]


