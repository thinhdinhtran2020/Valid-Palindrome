class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for character in s:
            if character.isalnum():
                new_s += character.lower()
        if new_s == new_s[::-1]:
            return True

                
def main():
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
main()
