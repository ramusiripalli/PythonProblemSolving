class Solution:
    def rotateArrayByOne(self, nums):
        """
        Rotates the given array by one position to the left.
        Example: [1, 2, 3, 4, 5] → [2, 3, 4, 5, 1]
        
        Args:
        nums (list): The input array to be rotated (modified in-place)
        """
        
        # Store the first element before overwriting it
        temp = nums[0]
        
        # Shift all elements one position to the left
        # Start from index 1 (second element) to end of array
        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]  # Move current element to previous position
        
        # Place the original first element at the end
        nums[-1] = temp

# Main method for testing
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test array
    nums = [1, 2, 3, 4, 5]
    print("Original array:", nums)
    
    # Rotate the array
    solution.rotateArrayByOne(nums)
    
    # Print the result
    print("Rotated array: ", nums)  # Output: [2, 3, 4, 5, 1]