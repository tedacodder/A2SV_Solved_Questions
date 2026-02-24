class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        i = 0
        j = 0
        start = -1

        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == 0:
                    start = i  # record possible start
                i += 1
                j += 1

                if j == len(needle):
                    return start  # full match found
            else:
                # reset search
                if start != -1:
                    # roll back i to the next position after the initial match start
                    i = start + 1
                else:
                    i += 1
                j = 0
                start = -1

        return -1
