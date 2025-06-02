'''
Insertion Sort

Insertion sort builds a sorted list one item at a time. It's much less efficient on large lists than merge sort because it's O(n^2), but it's actually faster (not in Big O terms, but due to smaller constants) than merge sort on small lists.
Explainer Video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: insertion sort

Assignment

Our influencers want to sort their affiliate deals by revenue. None of our users have more than a couple hundred affiliate deals, so we don't need an n * log(n) algorithm like merge sort. In fact, insertion_sort can be faster than merge_sort, and uses less of our server's memory.

Complete the insertion_sort function according to the given pseudocode:

    For each index in the input list:
        Set a j variable to the current index
        While j is greater than 0 and the element at index j-1 is greater than the element at index j:
            Swap the elements at indices j and j-1
            Decrement j by 1
    Return the list
'''

def insertion_sort(nums):
    for i in range(len(nums)):
        print(f"value of i: {i} \n length of nums: {len(nums)} \n range of nums: {range(len(nums))}")
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    print(nums)
    return nums

insertion_sort([1,10,12,4,3,7,4,9,45])
