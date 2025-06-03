'''
Selection Sort

Another sorting algorithm we never covered in-depth is called "selection sort". It's similar to bubble sort in that it works by repeatedly swapping items in a list. However, it's slightly more efficient than bubble sort because it only makes one swap per iteration.

Selection sort pseudocode:

    For each index:
        Set smallest_idx to the current index
        For each index from smallest_idx+1 to the end of the list:
            If the number at the inner index is smaller than the number at smallest_idx, set smallest_idx to the inner index
        Swap the number at the current index with the number at smallest_idx
    Return the sorted list

Assignment

Complete the selection_sort function.

It should sort the input list nums in ascending order using the selection sort algorithm. The function should then return the sorted list
'''

def selection_sort(nums):
    for i in range(len(nums)): # loop over the indices
        smallest_idx = i # setting value as the index
        for x in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]: # if the value at that index is smaller than the next
                smallest_idx = x # set the next small value as the smallest
            nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]  # swap
    return nums
