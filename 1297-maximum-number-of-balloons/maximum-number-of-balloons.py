class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        freq = {}

        # count frequency of input string
        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1

        # calculate answer
        return min(
            freq.get('b', 0),
            freq.get('a', 0),
            freq.get('l', 0) // 2,
            freq.get('o', 0) // 2,
            freq.get('n', 0)
        )