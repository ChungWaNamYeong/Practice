class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3=[]#合并后数组
        i=j=0 #ij比较指针
        flag=0 #检验先完成遍历的数组
        #检验空数组
        if nums1==[]:
            nums3=nums2
        elif nums2==[]:
            nums3=nums1
        else:
            while i<len(nums1) and j<len(nums2):
                if nums1[i]<=nums2[j]:
                    nums3.append(nums1[i])
                    i+=1
                    flag=1
                else:
                    nums3.append(nums2[j])
                    j+=1
                    flag=2
            #将剩余部分直接放到合并数组后
            if flag==1:
                for item in range(j,len(nums2)):
                    nums3.append(nums2[item])
            else:
                for item in range(i,len(nums1)):
                    nums3.append(nums1[item])
        length=len(nums3)
        if length%2:
            result=nums3[(length//2)]
        else:
            result=(nums3[length//2]+nums3[length//2-1])/2 #//保证int
        return result


    
            
        
