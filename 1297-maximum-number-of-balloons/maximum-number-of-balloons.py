class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        # frequency of balloon
        balloon_freq = {}

        for ch in "balloon":
            balloon_freq[ch] = balloon_freq.get(ch, 0) + 1

        # frequency of input string
        text_freq = {}

        for ch in text:
            text_freq[ch] = text_freq.get(ch, 0) + 1

        count = 0

        # repeatedly try to form "balloon"
        while True:

            can_make = True

            # check every character of balloon
            for ch in balloon_freq:

                # if character not enough
                if text_freq.get(ch, 0) < balloon_freq[ch]:
                    can_make = False
                    break

            # if cannot form balloon anymore
            if not can_make:
                break

            # decrease frequencies
            for ch in balloon_freq:
                text_freq[ch] -= balloon_freq[ch]

            # one balloon formed
            count += 1

        return count