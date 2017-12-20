import string

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        ans = None
        all_strs = string.ascii_uppercase + string.ascii_lowercase
        license_count = {}
        for char in licensePlate:
            if char in all_strs:
                c = char.lower()
                if c in license_count:
                    license_count[c] += 1
                else:
                    license_count[c] = 1

        for word in words:
            word_count = {}
            for char in word:
                if char in word_count:
                    word_count[char] += 1
                else:
                    word_count[char] = 1

            complete = True
            for char in license_count:
                if char not in word_count or word_count[char] < license_count[char]:
                    complete = False
                    break

            if complete:
                if not ans or len(word) < len(ans):
                    ans = word

        return ans

licensePlate = "1s3 PSt"; words = ["step", "steps", "stripe", "stepple"]
print(Solution().shortestCompletingWord(licensePlate, words))
licensePlate = "1s3 456"; words = ["looks", "pest", "stew", "show"]
print(Solution().shortestCompletingWord(licensePlate, words))
