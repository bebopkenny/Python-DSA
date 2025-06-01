'''
Merge Sort

Merge sort is a recursive sorting algorithm and it's quite a bit faster than bubble sort. It's a divide and conquer algorithm.:

    Divide: divide the large problem into smaller problems, and recursively solve the smaller problems
    Conquer: Combine the results of the smaller problems to solve the large problem

In merge sort we:

    Divide the array into two (equal) halves (divide)
    Recursively sort the two halves
    Merge the two halves to form a sorted array (conquer)

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Merge sort

Algorithm

The algorithm consists of two separate functions, merge_sort() and merge().

merge_sort() divides the input array into two halves, calls itself on each half, and then merges the two sorted halves back together in order.

The merge() function merges two already sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each only have one element. Those single element lists will be merged into a sorted list of length two, and we can build from there.

In other words, all the "real" sorting happens in the merge() function.
merge_sort() pseudocode

Input: A, an unsorted list of integers

    If the length of A is less than 2, it's already sorted so return it
    Split the input array into two halves down the middle
    Call merge_sort() twice, once on each half
    Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls

merge() pseudocode

Inputs: A and B. Two sorted lists of integers

    Create a new final list of integers.
    Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
    Use a loop to compare the current elements of A and B. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j. Continue until all items from one of the lists have been added.
    After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
    Return the final list.

Assignment

Our LockedIn influencers are complaining that when they sort their followers by follower count, it gets really slow if they have more than 1,000 followers (because we're using Bubble Sort). Let's speed it up for them with merge sort.

Complete the merge_sort and merge functions according to the described algorithms.
'''


def merge_sort(nums):
    a = len(nums)
    if a < 2:
        return nums
    middle = a // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge(left, right)

def merge(first, second):
    result = [] # create new list
    i, j = 0, 0 # indexes of first and second lists
    
    while i < len(first) and j < len(second): # the main loop
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
            continue
        else:
            result.append(second[j])
            j += 1
    while i < len(first):
        result.append(first[i])
        i += 1
    while j < len(second):
        result.append(second[j])
        j += 1
    return result





