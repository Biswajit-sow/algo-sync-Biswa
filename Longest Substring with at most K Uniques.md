## ***Longest Substring with at most K Uniques: means len(freq) <=k***


class Solution:
---

#### &nbsp;   def longestKSubstr(self, s, k):

#### &nbsp;       # code here

#### &nbsp;       freq={}

#### &nbsp;       n=len(s)

#### &nbsp;       current\_len=0

#### &nbsp;       low=0

#### &nbsp;       max\_len=-1

#### &nbsp;       

#### &nbsp;       if n<k:

#### &nbsp;           return -1

#### &nbsp;           

#### &nbsp;       for high in range(n):

#### &nbsp;           if s\[high] in freq:

#### &nbsp;               freq\[s\[high]] += 1

#### &nbsp;           else:

#### &nbsp;               freq\[s\[high]] = 1

#### &nbsp;           n1=len(freq)

#### &nbsp;           

#### &nbsp;           while(low < n and len(freq)>k):

#### &nbsp;               freq\[s\[low]]-=1

#### &nbsp;               

#### &nbsp;               if freq\[s\[low]]==0:

#### &nbsp;                   del freq\[s\[low]]

#### &nbsp;               low+=1

#### &nbsp;           

#### &nbsp;           n1=len(freq)

#### &nbsp;           if (n1<=k):

#### &nbsp;               current\_len=high-low+1

#### &nbsp;               max\_len=max(max\_len,current\_len)

#### &nbsp;       

#### &nbsp;       return max\_len

#### &nbsp;                   

#### &nbsp;           

#### &nbsp;       

