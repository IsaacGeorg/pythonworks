# class Solution:
#     def twoSum(self, nums, target):
#         self.nums=nums
#         self.target=target
#     def solve(self):
#         for i in range(0,len(self.nums)):
#             for j in range(i+1,len(self.nums)):
#                 lis=self.nums[i]+self.nums[j]
#                 if lis== self.target:
#                     return [i,j]
#         # return [i,j]
# nums=[3,3]
# target=9
# class_instance=Solution()
# class_instance.twoSum(nums,target)
# result=class_instance.solve()
# print(result)




class Solution:
    def twoSum(self, nums, target):
        prevMap={} # value:index
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return
    
class_instance=Solution()
class_instance.twoSum([2,7,11,12],9)

    
    
# print("Hello World")

# text="chris alan"
# text1=text.split(" ")
# print(text1)
# for i in text1:
#     print("".join(i.capitalize()),end="\t")


