def productExceptSelf(nums):
    n = len(nums)
    
    result = [1] * n

   
    prefix = 1
    for i in range(n):
        result[i] = prefix  
        prefix *= nums[i]   

    
    suffix = 1
    for i in range(n - 1, -1, -1):  
        result[i] *= suffix  
        suffix *= nums[i]   

    return result


nums = [-1, 1, 0, -3, 3]
output = productExceptSelf(nums)
print(output)
