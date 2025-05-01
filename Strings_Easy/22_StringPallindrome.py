class Solution:
    # Function to check if a given string is a palindrome
    def palindromeCheck(self, s):
        """
        Checks if the input string is a palindrome.
        A palindrome is a word that reads the same backward as forward.
        
        Args:
            s (str): The input string to be checked
            
        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        left = 0               # Initialize left pointer at start of string
        right = len(s) - 1     # Initialize right pointer at end of string

        # Iterate while left pointer is less than right pointer
        # This ensures we only check each pair of characters once
        while left < right:
            # If characters at current positions don't match, it's not a palindrome
            if s[left] != s[right]:
                return False
            
            # Move the pointers toward the center
            left += 1  # Move left pointer right by one position
            right -= 1  # Move right pointer left by one position
        
        # If all character pairs matched, it's a palindrome
        return True 

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test string
    str = "racecar"  # This is a known palindrome
    
    # Check if the string is a palindrome and print the result
    if solution.palindromeCheck(str):
        print(f"{str} is a palindrome.")
    else:
        print(f"{str} is not a palindrome.")