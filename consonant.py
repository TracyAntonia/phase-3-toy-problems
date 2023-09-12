# Constant values
def solve(s):
    # Calculates the value of a substring
    def substring_value(substring):
        return sum(ord(c) - ord('a') + 1 for c in substring)
    
    max_value = 0
    current_substring = ""

    # Iterates through a string
    for char in s:
        if char not in "aeiou":
            current_substring += char
        else:
            if current_substring:
                substring_val = substring_value(current_substring)
                max_value = max(max_value, substring_val)
            
            current_substring = ""

    # Checks if there's a consonant substring at the end
    if current_substring:
        substring_val = substring_value(current_substring)
        max_value = max(max_value, substring_val)

    return max_value

# Testing the codes
print(solve("zodiacs"))  
print(solve("strength"))  
