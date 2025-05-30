'''
O(n^2) - Order “N Squared”

O(n^2) grows in complexity much more rapidly. That said, for small and medium input sizes, these algorithms can still be very useful.

A common reason an algorithm falls into O(n^2) is by using a nested loop, where the number of iterations of each loop is equal to the number of items in the input:

for person_one in persons:
    for person_two in persons:
        # every combination of people
        # will go on a date... twice!
        go_on_date(person_one, person_two)

Assignment

LockedIn needs search capabilities! For now, we'll build something slow (and frankly awful) so we can see an n^2 algorithm in practice.

Complete the does_name_exist function. It should loop over all of the first/last name combinations in the first_names and last_names lists. If it finds a combination that matches the full_name it should return True. If the full name isn't found, it should return False instead.
Observe

When you run your completed code, notice how each successive call to does_name_exist takes quite a bit longer. Assuming the length of first_names and last_names is the same, each new name doesn't add n steps to the algorithm; the total number of steps grows quadratically with the size of the input, making the total work O(n^2).

If does_name_exist(10 names, 10 names) takes just 1 second to complete, then we can estimate:

    does_name_exist(100 names, 100 names) = 100 seconds
    does_name_exist(1000 names, 1000 names) = 10,000 seconds
    does_name_exist(10000 names, 10000 names) = 1,000,000 seconds
'''

def does_name_exist(first_names, last_names, full_name):
    matching_name = ""
    for i in first_names:
        for j in last_names:
            matching_name = f"{i} {j}"
            if matching_name == full_name:
                return True
    return False

def does_combo_exist(first_names, last_names, full_name):
    set_names = set() # creates a set so we can look up using hash map look up
    for i, x in zip(first_names, last_names): # looping through first and last name
        set_names.add(f"{i} {x}") # add first and last to the set 
    if full_name in set_names: # hash map loop up 
        return True

        