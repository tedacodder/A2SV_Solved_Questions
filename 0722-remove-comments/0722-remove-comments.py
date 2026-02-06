class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []              # final output lines
        inBlock = False          # state: are we inside /* ... */ ?
        buffer = ""              # collects valid characters for the current line

        # process input line by line
        for line in source:
            i = 0                # character pointer for the current line

            # scan characters left → right
            while i < len(line):
                # CASE 1: we are currently inside a block comment
                if inBlock:
                    # only thing that matters is: does the block end here?
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        inBlock = False     # exit block comment
                        i += 2              # skip "*/"
                    else:
                        i += 1              # ignore everything else
                else:
                    # CASE 2: we are NOT inside a block comment

                    # line comment starts → ignore rest of line
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break

                    # block comment starts → enter block
                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        inBlock = True
                        i += 2              # skip "/*"

                    # normal character → keep it
                    else:
                        buffer += line[i]
                        i += 1

            # after finishing a line:
            # only add buffer if we are NOT inside a block comment
            if not inBlock and buffer:
                result.append(buffer)
                buffer = ""                 # reset for next line

        return result
        