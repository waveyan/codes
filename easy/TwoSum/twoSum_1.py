class Solution:
    def twoSum(self, nums, target):
        """
        params:
        nums: List[int]
        target: int
        return List[int]
        [1,2,3] 5
        [-1,-2,-3] -5
        [0,1,-1,0] 0
        [-1,1] 0
        """
        length=len(nums)
        result=[]
        for i in range(length):
            temp=target
            result.clear()
            result.append(i)
            temp=temp-nums[i]
            for j in range(i+1,length):
                if nums[j]==temp:
                    result.append(j)
                    return result

if __name__ == '__main__':
    nums = [-3,4,3,90]
    target = 0
    print(Solution().twoSum(nums,target))



