# Checking for two positive numbers
def two_positives(a, b, c):
    # Count the number of positive integers
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    # Check for two positive integers
    return positive_count == 2

# Testing the codes
print(two_positives(4, 9, -3))  
print(two_positives(-4, 6, 0))  
print(two_positives(4, 6, 10))  