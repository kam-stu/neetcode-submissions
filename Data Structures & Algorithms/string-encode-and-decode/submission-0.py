class Solution:

    def encode(self, strs: List[str]) -> str:
        # loop through the list; save the length of the list and append it to before the word with a delimetter (lets use #)
        encoded = []

        for char in strs:
            length = len(char)
            encoded.append(f"{length}#{char}")

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # i can jump around to the next word, so a while loop would work best here
        while i < len(s):
            # initialize some j value to increment until it hits the delim
            j = i

            # always starting at a number.  "while" loop basically tells us how many digits there are 
            while s[j] != "#":
                j += 1

            # j is at the delim after looping over the digits
            length = int(s[i:j])

            # update i to the start of the word and j to the first digit of the next 
            i = j + 1
            j = i + length

            res.append(s[i:j])
            
            # update i to the first digit
            i = j
        return res
