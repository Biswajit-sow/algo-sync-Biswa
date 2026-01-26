## **Longest Substring with at Least K Uniques:**



#### class Solution:

#### &nbsp;   def longestKSubstr(self, s, k):

#### &nbsp;       if len(s) < k:

#### &nbsp;           return -1

#### &nbsp;       

#### &nbsp;       freq = {}

#### &nbsp;       max\_len = -1

#### &nbsp;       

#### &nbsp;       for high in range(len(s)):

&nbsp;           # freq\[s\[high]] = freq.get(s\[high], 0) + 1
		#or for frequency count in hashmap
---

#### &nbsp;	    if s\[high] in freq:

#### &nbsp;               freq\[s\[high]] += 1

#### &nbsp;           else:

#### &nbsp;               freq\[s\[high]] = 1

#### &nbsp;           

#### &nbsp;           # At least K uniques = condition met

#### &nbsp;           if len(freq) >= k:

#### &nbsp;               current\_len = high + 1  # Length from start to current position

#### &nbsp;               max\_len = max(max\_len, current\_len)

#### &nbsp;       

#### &nbsp;       return max\_len









## Example:

## 

## Example: s = "aaabbbccc", k = 2

#### 

#### Iteration high	s\[high]	  freq	            len(freq)	Condition(>=2)	max\_len	Window

#### 0	   0	'a'	{'a':1}			1	❌		-1	"a"

#### 1	   1	'a'	{'a':2}			1	❌		-1	"aa"

#### 2	   2	'a'	{'a':3}			1	❌		-1	"aaa"

#### 3	   3	'b'	{'a':3,'b':1}		2	✅		 4	"aaab"

#### 4	   4	'b'	{'a':3,'b':2}		2	✅		 5	"aaabb"

#### 5	   5	'b'	{'a':3,'b':3}		2	✅		 6	"aaabbb"

#### 6	   6	'c'	{'a':3,'b':3,'c':1}	3	✅		 7	"aaabbbc"

#### 7	   7	'c'	{'a':3,'b':3,'c':2}	3	✅		 8	"aaabbbc c"

#### 8	   8	'c'	{'a':3,'b':3,'c':3}	3	✅		 9	"aaabbbccc"



