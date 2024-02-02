class Solution(object):
    def isValid(self, s):
        stack=[]
        lefts={
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for elem in s:
            if len(stack)==0:
                stack.append(elem)
            else:
                if elem in ")]}" and stack[-1]==lefts[elem]:
                    stack.pop()
                else:
                    stack.append(elem)

        return True if len(stack)==0 else False
        