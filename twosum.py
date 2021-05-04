class Solution(object):
	def twoSum(self, nums, target):
		arr = {}
		for i in range(len(nums)):
			if nums[i] in arr:
				return [arr[nums[i]], i] 
			else: 
				arr[target - nums[i]] = i
