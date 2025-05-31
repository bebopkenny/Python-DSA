'''
Order 1

O(1) means that no matter the size of the input, there is no growth in the runtime of the algorithm. This is also referred to as a "constant time" algorithm.

In Python, a dictionary offers the ability to look items up by key, which is an operation that is independent of the size of the dictionary:

# this is a constant time lookup
org = organizations[org_id]

Dictionary lookups are O(1). Which is one of the reasons dictionaries and dictionary-equivalents in other languages are used all over the place.
Assignment

We need to be able to search our LockedIn user base more quickly! Our users are complaining that the search bar is painfully slow. You'll notice that if you run the code in its current state, it will take a very long time.

The find_last_name function takes

    names_dict: a dictionary of first_name -> last_name.
    first_name: a string.

If first_name is a key in the dictionary, find_last_name returns the associated last name. If the key is not found, it returns None.

Write the function so that it runs quickly! It should be O(1).
'''

def find_last_name(names_dict, first_name):
    if first_name not in names_dict: # checks if the first name is not in the names dictionary
        return None # returns none if not found     
    else: 
        return names_dict[first_name] # returns the last name if found