# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, nums, lower, upper):
            if lower == upper:
                return None

            mid = lower + (upper-lower) // 2
            node = TreeNode(nums[mid])
            node.left = self.helper(nums, lower, mid)
            node.right = self.helper(nums, mid+1, upper)

            return node
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums))
        
