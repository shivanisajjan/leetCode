# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
               "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
               "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        result = []
        for i in range(0, len(digits)):
            if i == 0:
                result = dic[digits[i]]
            else:
                keyVal = dic[digits[i]]
                temp = []
                for j in range(0, len(result)):
                    for k in range(0, len(keyVal)):
                        temp.append(result[j] + keyVal[k])
                result = temp
        return result
    
    
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        leng = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in result:
                    leng = max(leng, len(result))
                    result = []
                    break
                result.append(s[j])
        return leng




