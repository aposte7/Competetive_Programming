class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res=[]
        for i in range(n-1):
            min = i
            for j in range(i+1,n):
                if nums[j]<nums[min]:
                    min=j
            nums[min],nums[i]= nums[i],nums[min]
            if nums[i]==target:
                res.append(i)
        if nums[n-1]==target:
                res.append(n-1)
        return res
        
        

        