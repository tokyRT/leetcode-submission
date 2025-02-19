class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = int("".join([str(i) for i in digits])) + 1
        res = str(n)

        return [int(i) for i in res]
        