s = "Marge, let's \"[went].\" I await {news} telegram."
symbols = [',', '.', ':', ' ', '@', '!', '?', ';', '/', '#', '&', '*', '(', ')', '[', ']', '_', '-', '{', '}', '\\', "'"]
for i in symbols:
    s = s.replace(i, '')
s = s.lower()
print(s, s[::-1])


class Solution:
    def isPalindrome(self, s: str) -> bool:
        symbols = [',', '.', ':', ' ', '@', '!', '?', ';', '/', '#', '&', '*', '(', ')', '[', ']', '_', '-', '{', '}', '\\', "'", '"', '`']
        for i in symbols:
            s = s.replace(i, '')
        s = s.lower()
        return s == s[::-1]