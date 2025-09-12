class Solution:
    def doesAliceWin(self, s: str) -> bool:

        return len(set(s).intersection({'a','e','i','o','u'})) > 0