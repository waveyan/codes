class Solution:
    def removeDuplicates(self, nums: list) -> int:
        '''Confused why the returned value is an integer but your answer is an array?
        Note that the input array is passed in by reference, which means modification
         to the input array will be known to the caller as well.'''
        length=len(nums)
        count = length
        if length>0:
            last=nums[0]
        i=1
        while i<len(nums):
            if nums[i]==last:
                count=count-1
                nums.pop(i)
            else:
                last = nums[i]
                i=i+1

        return count

if __name__=='__main__':
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))




