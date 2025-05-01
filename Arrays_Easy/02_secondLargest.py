from typing import List

class Solution:
    def secondLargestElement(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return -1

        largest =  float('-inf')
        second_largest =  float('-inf')

        for num in nums:

            if num > largest:
                second_largest = largest
                largest = num

            elif num > second_largest and num != largest:
                second_largest = num

        return -1 if second_largest == float('-inf') else second_largest

# Main function
if __name__ == "__main__":
    nums = [1, 2, 7, 6, 7, 6]

   #Creating an instance of the Solution class
    sol = Solution()

    result = sol.secondLargestElement(nums)
    print("Second largest is:", result)
