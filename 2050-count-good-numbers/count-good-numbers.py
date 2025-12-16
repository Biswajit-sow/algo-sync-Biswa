class Solution:
    def countGoodNumbers(self, n: int) -> int:
        Mod=(10**9+7)
        even_pos=(n+1)//2
        odd_pos=n//2
        
        output=(pow(5,even_pos,Mod)*pow(4,odd_pos,Mod))%Mod
        return output
        
        