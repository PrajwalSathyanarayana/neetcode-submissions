class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right  = len(nums)-1
        mid = (left + right)//2
        while left <= right:
            if target == nums[mid]:
                return mid
            else:
                if nums[left]<=nums[mid]:
                    if nums[left]<=target<=nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid]<=target<=nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
            mid = (left + right)//2
        return -1