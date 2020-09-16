# LeetCode_Exercise

## ***Program1.py***

   **Leetcode :- First Program**
   
   Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
 
>Examples:

     Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1]
     Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
     Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]
 
>Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


## ***Program2.py***

   **Leetcode :- Second Program**
   
   Given a string s, find the length of the longest substring without repeating characters.
   
>Examples:

     Example 1:
          Input: s = "abcabcbb"
          Output: 3
          Explanation: The answer is "abc", with the length of 3.
     Example 2:
          Input: s = "bbbbb"
          Output: 1
          Explanation: The answer is "b", with the length of 1.
     Example 3:
          Input: s = "pwwkew"
          Output: 3
          Explanation: The answer is "wke", with the length of 3.
                       Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.                  
    Example 4:              
          Input: s = ""
          Output: 0
   
>Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


## ***Program3.py***

   **Leetcode :- Third Program**
   
   
   Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Follow up: The overall run time complexity should be O(log (m+n)).


>Examples:

     Example 1:
          Input: nums1 = [1,3], nums2 = [2]
          Output: 2.00000
          Explanation: merged array = [1,2,3] and median is 2.
     Example 2:
          Input: nums1 = [1,2], nums2 = [3,4]
          Output: 2.50000
          Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
     Example 3:
          Input: nums1 = [0,0], nums2 = [0,0]
          Output: 0.00000                  
     Example 4:              
          Input: nums1 = [], nums2 = [1]
          Output: 1.00000
     Example 5:              
          Input: nums1 = [2], nums2 = []
          Output: 2.00000
          
   
>Constraints:

     - nums1.length == m
     - nums2.length == n
     - 0 <= m <= 1000
     - 0 <= n <= 1000
     - 1 <= m + n <= 2000
     - -106 <= nums1[i], nums2[i] <= 106


