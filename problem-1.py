# Time Complexity :O(logn)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no


# Your code here along with comments explaining your approach in three sentences only
# check if the current segement is already sorted then nums[l] would be the pivot, if not then get the mid
# and check if it's left neighbor is larger if it is then the mid would be the pivot, if not divide into segments, left of mid and right of mid
# then chose the segment which is not sorted, bcause min belongs in the not sorted segment and repeat until we find the pivot  

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]<=nums[r]:
                return nums[l]
            k=(l+r)//2
            if k!=0 and nums[k]<nums[k-1]:
                return nums[k]
            elif nums[l] <= nums[k]:
                l = k+1
            else:
                r = k-1
        return -1
