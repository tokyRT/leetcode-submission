class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        retenu = 1
        res = []
        i=len(digits)-1
        while i >= 0:
            tmp = digits[i] + 1 if retenu == 1 else digits[i]
            res.append(tmp % 10)
            if tmp == 10: retenu = 1
            else: retenu = 0

            i-=1

        if retenu == 1:
            res.append(1)
            retenu = 0
        res.reverse()

        return res
        