class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res=0
        seen=True
        while seen:
            for i in "balloon":
                if i in text:
                    text=text.replace(i,"",1)
                    if i=='n':res+=1
                else:
                    seen=False
                    break
        return res