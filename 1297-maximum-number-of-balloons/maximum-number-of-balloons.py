class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_freq = {}

        for ch in "balloon":
            balloon_freq[ch] = balloon_freq.get(ch, 0) + 1 

        text_freq = {}

        for ch in text:
            text_freq[ch] = text_freq.get(ch, 0) + 1
        
        res=float('inf')
        for  i in balloon_freq:
           
            fballon=balloon_freq[i]
            if i in text_freq:
                ftext=text_freq[i]
            else:
                ftext=0
            times=ftext//fballon
            res= int(min(res,times))
        return res 



