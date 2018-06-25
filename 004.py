class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        ln1 = len(nums1)
        ln2 = len(nums2)
        ln = ln1 + ln2
        count, i1, i2 = 0, 0, 0
        odd = ln % 2 == 1 # нечетный

        num1 = nums1[0] if ln1 > 0 else None
        num2 = nums2[0] if ln2 > 0 else None
        if num1 != None and num2 != None:
            prev_num = min(num1, num2)
            
        if num1 != None and num2 == None:
            prev_num = num1

        if num1 == None and num2 != None:
            prev_num = num2

        while count < ln:

            num1 = nums1[i1] if i1 < ln1 else None
            num2 = nums2[i2] if i2 < ln2 else None
            if num1 != None and num2 != None:
                if num1 <= num2:
                    num = num1
                    i1 += 1
                else:
                    num = num2
                    i2 += 1
            
            if num1 != None and num2 == None:
                num = num1
                i1 += 1

            if num1 == None and num2 != None:
                num = num2
                i2 += 1

            if count == ln // 2:
                if odd:
                    return num
                else:
                    return (num + prev_num) / 2

            count +=1
            prev_num = num

print(Solution().findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22], [0,6]))
#print(Solution().findMedianSortedArrays([], [1]))
#print(Solution().findMedianSortedArrays([1, 3], [2]))
#print(Solution().findMedianSortedArrays([1, 2], [3, 4]))