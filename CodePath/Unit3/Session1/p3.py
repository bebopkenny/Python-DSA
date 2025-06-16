'''
Problem 3: Check Symmetry in Post Titles

As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.
'''

def is_symmetrical_title(title):
    left = 0 # left starting index
    right = len(title) - 1 # right starting index
    while left <= right: # while the left doesnt cross over to right
        # Skip over white spaces
        if title[left] == ' ': 
            left += 1
        elif title[right] == ' ':
            right -= 1
        # if the left and right index do not match return False    
        elif title[left].lower() != title[right].lower():
            return False
        # Continue by moving the indecies
        else:
            left += 1
            right -= 1
    return True
        
            

          

# Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

# Example Output:

# True
# False
