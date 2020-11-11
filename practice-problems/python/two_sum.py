'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 105
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
'''

# def twoSum(nums: list, target: int) -> list:
#   # for each element of list, iterate over list for comparision
#   for i in range(len(nums)):
#     for j in range(len(nums)):
#       # skip self for comparison
#       if j == i: continue
#       # return elements if they add up to the target value
#       if nums[i] + nums[j] == target:
#         return [i, j]
#   return

class Solution:
  def twoSum(self, nums, target):
    hash_table = {}
    for i in range(len(nums)):
      difference = target - nums[i]
      if difference not in hash_table:
        hash_table[nums[i]] = i
      else:
        return [hash_table[difference], i] 


soultion_two = Solution()

print(soultion_two.twoSum([2,1,11,15, 7], 9))

# solution = twoSum([2,7,11,15], 9)

# print(solution)