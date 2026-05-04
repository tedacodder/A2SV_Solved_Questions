class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # ---------------------------------------------------------
        # DFS / Backtracking Function
        #
        # Parameters:
        # index -> current position in the string
        # a     -> previous number
        # b     -> second previous number
        #
        # Goal:
        # Check whether the remaining substring follows
        # the additive sequence rule.
        # ---------------------------------------------------------
        def dfs(index, a, b):

            # If we reached the end of the string successfully,
            # then the sequence is valid.
            if index == n:
                return True

            # The next expected number in the sequence
            next_num = a + b

            # Convert to string because the input is a string
            next_str = str(next_num)

            # Check whether the remaining substring
            # starts with the expected number
            if num.startswith(next_str, index):

                # Move forward by length of next number
                return dfs(
                    index + len(next_str),
                    b,
                    next_num
                )

            # If expected number does not match,
            # this path is invalid
            return False

        # ---------------------------------------------------------
        # Try every possible first number
        # ---------------------------------------------------------
        for i in range(1, n):

            # First number
            first = num[:i]

            # -----------------------------------------------------
            # Leading zero check
            #
            # Invalid:
            # "01", "001", etc.
            #
            # Valid:
            # "0"
            # -----------------------------------------------------
            if len(first) > 1 and first[0] == '0':
                break

            # Convert first number to integer
            a = int(first)

            # -----------------------------------------------------
            # Try every possible second number
            # -----------------------------------------------------
            for j in range(i + 1, n):

                # Second number
                second = num[i:j]

                # Leading zero check for second number
                if len(second) > 1 and second[0] == '0':
                    break

                # Convert second number to integer
                b = int(second)

                # -------------------------------------------------
                # Start checking additive sequence
                #
                # j is the next unread position
                # -------------------------------------------------
                if dfs(j, a, b):
                    return True

        # No valid additive sequence found
        return False
