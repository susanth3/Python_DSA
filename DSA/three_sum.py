class Solution:
    def threeSum(self, nums):
        i = 0
        n = len(nums)
        result = []
        nums.sort()
        while i < n:
            if (i == 0 or (i - 1 >= 0 and nums[i] != nums[i-1])):
                firstElement = nums[i]
                target = 0 - firstElement
                pairs = self.twoSum(nums,i+1,n-1,target)
                for pair in pairs:
                    triplet = [firstElement,pair[0],pair[1]]
                    result.append(triplet)
            i += 1
        
        return result  
        
        
    def twoSum(self,nums,start,end,target):
        pairs = []
        f = start
        s = end
        
        while f < s:
            if f - 1 >= start and nums[f] == nums[f-1]:
                f += 1
                continue
            if s + 1 <= end and nums[s] == nums[s+1]:
                s -= 1
                continue
            if nums[f] + nums[s] < target:
                f += 1
            elif nums[f] + nums[s] > target:
                s -= 1
            else:
                pair = [nums[f],nums[s]]
                pairs.append(pair)
                f += 1
        return pairs
        

nums = [5,4,6]
s = Solution()
print(s.threeSum(nums))