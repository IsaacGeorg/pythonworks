# nums=[0,1,2,4,5,7]
# continu=set()
# discontinu=[]
# for i in range(0,len(nums)-1):
#     j=i+1
#     diff=nums[i]-nums[j]
    
#     if diff==-1:
#         a=nums[i]
#         b=nums[j]
#         continu.add(a)
#         continu.add(b)
#         print(continu)
#     else:
#         discontinu.append(nums[j])
#         print(discontinu)


# # Output: "0->2","4->5","7"


# nums = [0, 1, 2, 4, 5, 7]
# ranges = []  
# start = nums[0]  

# for i in range(1, len(nums)):
#     if nums[i] != nums[i - 1] + 1:  
        
#         if start == nums[i - 1]:
#             ranges.append(f"{start}")  
#         else:
#             ranges.append(f"{start}->{nums[i - 1]}")  
#         start = nums[i]  


# if start == nums[-1]:
#     ranges.append(f"{start}")
# else:
#     ranges.append(f"{start}->{nums[-1]}")

# output = ', '.join(ranges)
# print(output)



# nums = [0, 1, 2, 4, 5, 7]
# ranges = [] 
# start = nums[0]  
# for i in range(1, len(nums)):
#     if nums[i] != nums[i - 1] + 1:  
#         if start == nums[i - 1]:
#             ranges.append(f"{start}")  
#         else:
#             ranges.append(f"{start}->{nums[i - 1]}")  

# if start == nums[-1]:
#     ranges.append(f"{start}")
# else:
#     ranges.append(f"{start}->{nums[-1]}")

# print(ranges)




nums = [0,2,3,4,6,8,9]
ranges = []  
start = nums[0] 

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1] + 1: 
       
        if start == nums[i - 1]:
            ranges.append(f"{start}") 
        else:
            ranges.append(f"{start}->{nums[i - 1]}")  
        start = nums[i] 


if start == nums[-1]:
    ranges.append(f"{start}")
else:
    ranges.append(f"{start}->{nums[-1]}")

print(ranges)






