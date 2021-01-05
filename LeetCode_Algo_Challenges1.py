"""
Leetcode Challenge Questions in Python
File 1
Easy Questions
Jeffrey Kwarsick
"""
"""
1. TWO SUM
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return([hash_table[target-num],i])
                break
            hash_table[num] = i
        return([])
        
"""
7. REVERSE INTEGER
Given a 32-bit signed integer, reverse digits of an integer.
"""
class Solution:
    def reverse(self, x: int) -> int:
        temp = list(str(x))
        if x<0:
            res = temp[:0:-1]
            out=int(''.join(res))
            if out > pow(2,31) or out < -1*pow(2,31):
                return(0)
            else:
                return(out*-1)
        else:
            res = temp[::-1]
            out=int(''.join(res))
            if out > pow(2,31) or out < -1*pow(2,31):
                return(0)
            else:
                return(out)
                
"""
9. PALINDROME NUMBER
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        rev = tmp[::-1]
        if tmp == rev:
            return(True)
        else:
            return(False)
            
"""
13. ROMAN TO INTEGER
Given a roman numeral, convert it to an integer.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        temp = list(s)
        res = []
        for i in range(len(temp)):
            res.append(roman[temp[i]])
    
        result = 0
        i = 0
  
        while (i < len(res)):
            s1 = res[i]
            if (i+1 < len(s)): 
                # Getting value of symbol s[i+1] 
                s2 = res[i+1]
                if (s1 >= s2):
                    result += s1
                    i = i + 1
                else:
                    result = result + s2 - s1 
                    i = i + 2
            else: 
                result = result + s1 
                i = i + 1
        return(result)
        
"""
21. MERGE TWO SORTED LISTS
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
                
"""
26. REMOVE DUPLICATES FROM SORTED ARRAY
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1

        return k
"""
69. SQRT(X)
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        return(int(sqrt(x)))