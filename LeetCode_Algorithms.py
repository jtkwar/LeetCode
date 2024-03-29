"""
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        def dfs(root, targetSum):
            if not root:
                if not targetSum: return True
                else: return False
            if root.left and root.right:
                return dfs(root.left, targetSum-root.val) or dfs(root.right, targetSum-root.val)
            else:
                if not root.right:
                    return dfs(root.left, targetSum-root.val)
                if not root.left:
                    return dfs(root.right, targetSum-root.val)
        return dfs(root, targetSum)
		
"""
125. Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuation = "!@#$%^&*()_+<>?:.,;\/[]{}-`"
        for c in s:
            if c in punctuation:
                s = s.replace(c, "")
        s = s.replace(" ", "")
        s = s.replace('"', '')
        s = s.replace("'", "")
        s = s.lower()
        if s == s[::-1]:
            return True
        else:
            return False
			
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        for i in s.lower():
            if i.isalnum():
                p += i
        else:
            return p == p[::-1]
			
"""
168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=""
        while n:
            n=n-1
            ans=abc[n%26]+ans
            n=n//26
        return ans
		
"""
169. Majority Element
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorElement = None
        for num in nums:
            if count == 0:
                majorElement = num
            count += 1 if majorElement == num else -1
        return majorElement
		
"""
4. Median of Two Sorted Arrays
HARD
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        out = nums1 + nums2
        out = sorted(out)
        n = len(out)
        if n == 1:
            return out[0]
        elif n%2 == 0:
            first_mid  = int(len(out) / 2) - 1
            second_mid = int(len(out) / 2)
            median = (out[first_mid] + out[second_mid]) / 2
        else:
            mid = int(len(out) / 2)
            median = out[mid]
        return median
		
"""
191. Number of 1 Bits
EASY
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = "{0:b}".format(n)
        count = 0
        for c in s:
            if c == '1':
                count += 1
        return count
        
"""
121. Best Time to Buy and Sell Stock
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0] # at the begining the minimum price is the first price
        profit = 0 # at the begining the minimum  profit is zero
        
        for i in range(1,len(prices)):
            #if the current price is less than the previous buy price ; update the buy_price
            if prices[i] < buy_price:
                buy_price = prices[i]
            else: # if not check if you sell with the current price would you get better profit than the previous one
                profit = max(profit, prices[i]-buy_price) # compare the previous profit with the current profit
                
        return profit