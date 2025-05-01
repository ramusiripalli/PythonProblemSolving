class Solution:
    def right_rotate(self,nums,k):
        n = len(nums)
        temp = []
        for i in range(n-k,n):
            temp.append(nums[i])
        
        for i in range(0,n):
            nums[n-i-1] = nums[n-k-i]

      
if __name__ == "__main__":
    sol = Solution()
    nums=[1,2,3,4,5,6]
    k=2
    res = sol.right_rotate(nums,k)
    print(f"Result of the array is : ", res)