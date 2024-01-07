class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0
        for word in words:
            if line_length + len(word) + len(line) > maxWidth:
                total_spaces = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * total_spaces)
                else:
                    spaces_between_words = total_spaces // (len(line) - 1)
                    extra_spaces = total_spaces % (len(line) - 1)
                    justified_line = ''
                    for i in range(len(line) - 1):
                        justified_line += line[i] + ' ' * spaces_between_words
                        if i < extra_spaces:
                            justified_line += ' '
                    justified_line += line[-1]
                    result.append(justified_line)
                line = []
                line_length = 0
            line.append(word)
            line_length += len(word)

        # Last line handling (left-justified)
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result
