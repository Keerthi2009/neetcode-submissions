class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1=[]
        for i,num in enumerate(nums):
            num1.append([num,i])
        num1.sort()
        i=0
        j=len(num1)-1
        total=0 
        while(i<j):
            total = num1[i][0]+num1[j][0]
            if total==target :
             return [min(num1[i][1],num1[j][1]),
                    max(num1[i][1],num1[j][1])]

            if total<target:
                i=i+1
            else:
                j=j-1