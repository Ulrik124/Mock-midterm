def calculate_days_since_birthday(birthday):
    # Split the birthday string and convert to integers
    day, month, year = map(int, birthday.split('-'))

    # Manually set the current date (you would replace these values with the actual current date)
    current_day = 1  # for example
    current_month = 3  # for example
    current_year = 2024  # for example

    # Calculate full years between birth year and current year
    full_years = current_year - year - 1  # Subtract 1 to exclude current year and birth year

    # Calculate total days (ignoring leap years)
    total_days = full_years * 365

    return total_days


# Example usage
birthday = "21-01-2003"
print(calculate_days_since_birthday(birthday))


7
7
14
abcabcabcabc
``` &#8203;``【oaicite:0】``&#8203;








def find_pattern(text):
    count = 0  # Initialize a counter for the number of matches
    i = 0  # Start with the first character of the text

    # Loop over the text until there's less than 4 characters left,
    # because we need at least 4 characters to form a pattern starting with 'C' and ending with 'jeb'
    while i < (len(text) - 3):
        # If the current character is 'C' and the next three characters are 'jeb'
        if text[i] == 'C' and text[i + 1:i + 4] == 'jeb':
            count += 1  # Increment the count
            i += 4  # Move the index past the found pattern
        else:
            i += 1  # Move to the next character and continue searching

    return count


# Example usage:
example_text = "CjebCjebCjeb"
print(find_pattern(example_text))  # This should return 3