# https://leetcode.com/problems/assign-cookies/submissions/


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count,i,j = 0,0,0
        while i<len(g) and j<len(s):
            if s[j] >= g[i]:
                count += 1
                i+=1
                j+=1
            else:
                j+=1
        return count


# https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row, col = rowIndex + 1, (2 * (rowIndex + 1)) - 1
        ret = [[0 for i in range(col)] for j in range(row)]
        ret[0][col // 2] = 1
        # print(ret)
        for i in range(1, row):
            j = row - i - 1
            while (j <= row + i - 1):
                if j == 0:
                    ret[i][j] = ret[i - 1][j + 1]
                elif j == (col - 1):
                    ret[i][j] = ret[i - 1][j - 1]
                else:
                    ret[i][j] = ret[i - 1][j + 1] + ret[i - 1][j - 1]
                j += 2

            if i == row - 1:
                return ([k for k in ret[i] if k != 0])
        return [1]


# https://leetcode.com/problems/merge-sorted-array/submissions/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m
        for num in nums2:
            nums1[i] = num
            i += 1
        nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # My Solution
#         i,j = 0,0
#         while i < len(nums1):
#             if(nums1[i] < nums2[j]):
#                 i+=1
#             else:
#                 nums1 = self.push(nums1,nums2[j],i)
#         print(nums1)

#     def push(self,nums1,nums,index) -> List[int]:
#         temp = nums1[index]
#         nums1[index] = nums
#         temp2 = 0
#         for i in range(index+1,len(nums1)):
#             temp2 = nums1[i]
#             nums1[i] = temp
#             temp = temp2
#         return nums1



