def find_pattern(text):
    count = 0
    i = 0
    while i < len(text):
        if text[i] == 'C':
            end_index = text.find('jeb', i + 1)
            if end_index != -1:
                count += 1
                i = end_index + 3
            else:
                i += 1
        else:
            i += 1
    return count

# Example usage:
example_text = "CabcjebCdefgjebChijjeb"
print(find_pattern(example_text))
