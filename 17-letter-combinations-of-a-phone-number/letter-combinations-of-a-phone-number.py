class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return[]
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result=[""]
        
        for digit in digits: # for digit in input
            temp=[]
            for combination in result: #for each existing combination
                for letter in digit_to_letters[digit]: #for each letter mapped to digit
                    temp.append(combination+letter) #combine them
            result=temp
        return result

