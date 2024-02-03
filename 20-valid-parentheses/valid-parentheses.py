class Solution(object):
    def isValid(self, s):
        v=s
        while True:
            if v=="": return True
            tmp=v
            print(v)
            v=v.replace("()", "")
            v=v.replace("[]", "") 
            v=v.replace("{}", "")
            print(v)
            if v==tmp: return False
        return True
        