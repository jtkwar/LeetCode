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
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for letters in zip(*strs):
            if len(set(letters)) == 1:
                res.append(letters[0])
            else:
                break
        return "".join(res)
        
"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")","[":"]","{":"}"}
        rev = s[::-1] #Let's reverse the string bcz the key-value is stored in proper order
        stk = [] #Empty stack
    
        for i in rev:
            if i not in d:
                stk.append(i)
            elif len(stk) == 0 or stk.pop() != d[i]: #len(stk) == 0 is required where input = "((", here nothing will be inserted in stack
                return(0)
        
        if len(stk)==0: #Every element is popped out
            return 1
            
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
27. REMOVE ELEMENT
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = (item for item in nums if item != val)
        return len(nums)
        
"""
35. SEARCH INSERT POSITION
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        copy_nums = nums
        try:
            return nums.index(target)
        except:
            copy_nums.append(target)
            return sorted(copy_nums).index(target)

"""
58. LENGTH OF LAST WORD
Given a string s consists of some words separated by spaces,
return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = list(filter(None, s.split(" ")))
        return len(word[-1]) if len(word) else 0
     
"""
66. PLUS ONE
Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) > 0: 
            num = int("".join([str(i) for i in digits])) + 1
            num = [int(i) for i in str(num)]
        if len(num) < len(digits):
            num = [0] * (len(digits) - len(num)) + num
        return num

"""
67. ADD BINARY
Given two binary strings a and b, return their sum as a binary string
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = int(a, 2) + int(b, 2)
        return(str(bin(out)[2:]))

"""
69. SQRT(X)
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        return(int(sqrt(x)))

"""
70. CLIMBING STAIRS
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        s1, s2, s3 = 0, 1, 2
        while n > 2:
            s1, s2 = s2, s3
            s3 = s1 + s2
            n -= 1
        return s3