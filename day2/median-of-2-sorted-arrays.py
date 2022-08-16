class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=[]
        l=len(nums1)+len(nums2)
        c1=0
        c2=0
        for i in range(int(l/2)+1):
            if(c1>len(nums1)-1):
                d=int(l/2)+1-i
                merged.extend(nums2[c2:c2+d])
                break
            elif(c2>len(nums2)-1):
                d=int(l/2)+1-i
                merged.extend(nums1[c1:c1+d])
                break
            else:
                if(nums1[c1]>nums2[c2]):
                    merged.append(nums2[c2])
                    c2+=1
                else:
                    merged.append(nums1[c1])
                    c1+=1
        
        if l%2==0:
            return (merged[-1]+merged[-2])/2
        else:
            return merged[-1]