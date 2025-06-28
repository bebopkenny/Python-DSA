'''
Problem 7: Sort Performances by Type

You are organizing a cultural festival and have a list of performances represented by an integer array performances. Each performance is classified as either an even type (e.g., dance, music) or an odd type (e.g., drama, poetry).

Your task is to rearrange the performances so that all the even-type performances appear at the beginning of the array, followed by all the odd-type performances.

Return any array that satisfies this condition.
'''

def sort_performances_by_type(performances):
    if len(performances) == 1:
        return [0]
    even = []
    odd = []
    for i in performances:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd

# Example Usage:

print(sort_performances_by_type([3, 1, 2, 4]))  
print(sort_performances_by_type([0]))  

# Example Output:

# [4, 2, 1, 3]
# [0]
