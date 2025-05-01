class Solution:
  def sumOfAllElements(self,nums):
    # Initialize the sum variable to 0
    total_sum = 0

    # Iterate through each element in the list
    for num in nums:
      # Add the current element to the total sum
      total_sum += num

    # Return the final sum
    return total_sum
# Main function 
if __name__ == "__main__":
  nums = [1, 2, 7, 6, 7, 6]

  # Creating an instance of the Solution class
  sol = Solution()

  result = sol.sumOfAllElements(nums)
  print("Sum of all elements is:", result)