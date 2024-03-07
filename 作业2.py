'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
请找出给定目标值在数组中的开始位置和结束位置。如果数组中不存在目标值 target，返回 [-1,-1]。
'''
def halfsearch(nums,target):
    if not (isinstance(nums,(list,tuple)) and isinstance(target,(int,float))):
        print('传入参数有误！')
        return
    low,high=0,len(nums)-1
    mid=(low+high)//2
    l=r=-1
    #开始与结束位置下标
    while low<=high: #
        if nums[mid]>target:
            high=mid-1
        elif nums[mid]<target:
            low=mid+1
        else:
            l=r=mid
            break
        mid=(low+high)//2
    if l!=-1:
        while l>0 and nums[l-1]==target:
            l-=1
        while r<len(nums)-1 and nums[r+1]==target:
            r+=1
    return [l,r]

print(halfsearch([1],1))



