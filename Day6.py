
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/


# can be done still better
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        civilian_count = {}
        prev = mat[0].count(1)
        for i in range(len(mat)):
            civilian_count[i] = mat[i].count(1)
        civilian_count = dict(sorted(civilian_count.items(), key=lambda kv: (kv[1], kv[0])))
        result = []
        for keys in civilian_count.keys():
            if k == 0:
                break
            result.append(keys)
            k -= 1
        return result



# https://leetcode.com/problems/flipping-an-image/

# My Solution

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image