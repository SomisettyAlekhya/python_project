import re

class Poem:
    def __init__(self, filename):
        self.items = []
        fileObject = open(filename, "r")
        for line in fileObject:
            self.items.append(line)
        fileObject.close()

    # Showing the data
    def show(self):
        result = []
        for line in self.items:
            result.append(line.strip())
        return result

    # using enumerate 
    def clean(self):
        pattern = "[^a-zA-Z]"
        cleaned_lines = []

        index = 0
        for line in self.items:
            new_line = re.sub(pattern, " ", line)
            cleaned_lines.append([index, new_line])
            index += 1

        return cleaned_lines

    # using map 
    def clean_1(self):
        pattern = "[^a-zA-Z]"
        cleaned_list = []

        for line in self.items:
            new_line = re.sub(pattern, " ", line)
            cleaned_list.append(new_line)

        return cleaned_list

    # list comprehension 
    def clean_2(self):
        pattern = "[^a-zA-Z]"
        final_result = []

        for line in self.items:
            modified_line = re.sub(pattern, " ", line)
            final_result.append(modified_line)

        return final_result

    # Get lines containing a word 
    def getLines(self, word):
        pattern = r"[^a-zA-Z]"
        matched_lines = [word]

        index = 0
        for line in self.items:
            cleaned_line = re.sub(pattern, " ", line)
            if word.lower() in cleaned_line.lower():
                matched_lines.append((index, line))
            index += 1

        return matched_lines
