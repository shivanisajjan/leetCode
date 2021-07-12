https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")" : "(" , "}" : "{" , "]" : "["}
        for i in range(0,len(s)):
            if((s[i] == "(") or (s[i] == "{") or (s[i] == "[")):
                stack.append(s[i])
            else:
                if len(stack) > 0 and stack[-1] == dic[s[i]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


https://leetcode.com/problems/reverse-string/


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s)-1
        while first < last:
            s[first],s[last] = s[last],s[first]
            first,last = first+1,last-1


https://leetcode.com/problems/first-unique-character-in-a-string/submissions/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        repdic = {}
        for i in range(0,len(s)):
            if s[i] not in dic:
                if s[i] not in repdic:
                    dic[s[i]] = i
            else:
                repdic[s[i]] = i
                dic.pop(s[i])
        for key in dic:
            return dic[key]
        return -1




