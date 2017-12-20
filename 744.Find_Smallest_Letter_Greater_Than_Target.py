class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ans = None
        for letter in letters:
            if letter > target and (not ans or letter < ans):
                ans = letter
        return ans if ans else min(letters)

def test(letters, target, output):
    result = Solution().nextGreatestLetter(letters, target)
    print(result == output, letters, target, output)

# Input:
letters = ["c", "f", "j"]
target = "a"
Output = "c"
test(letters, target, Output)

# Input:
letters = ["c", "f", "j"]
target = "c"
Output = "f"
test(letters, target, Output)

# Input:
letters = ["c", "f", "j"]
target = "d"
Output = "f"
test(letters, target, Output)

# Input:
letters = ["c", "f", "j"]
target = "g"
Output = "j"
test(letters, target, Output)

# Input:
letters = ["c", "f", "j"]
target = "j"
Output = "c"
test(letters, target, Output)

# Input:
letters = ["c", "f", "j"]
target = "k"
Output = "c"
test(letters, target, Output)

letters = ['a', 'b']
target = "z"
Output = "a"
test(letters, target, Output)
