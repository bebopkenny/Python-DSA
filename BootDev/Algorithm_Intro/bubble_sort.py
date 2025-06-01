'''
Bubble Sort

Wait, if the standard sorted() function exists, why should we learn to write a sorting algorithm from scratch?

john f kennedy

In all seriousness, in this chapter we'll be building some of the most famous sorting algorithms from scratch because:

    It's good to understand how they work under the hood
    It's great algorithmic thinking practice
    It's fun! (at least for me)

Bubble sort is a very basic sorting algorithm named for the way elements "bubble up" to the top of the list.

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Bubble sort

Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. It continues to loop over the slice until the whole list is completely sorted. Here's the pseudocode:

    Set swapping to True
    Set end to the length of the input list
    While swapping is True:
        Set swapping to False
        For i from the 2nd element to end:
            If the (i-1)th element of the input list is greater than the ith element:
                Swap the (i-1)th element and the ith element
                Set swapping to True
        Decrement end by one
    Return the sorted list

Assignment

While our avocado toast influencers were happy with our search functionality, now they want to be able to sort all their followers by follower count. Bubble sort is a straightforward sorting algorithm that we can implement quickly, so let's do that!

Complete the bubble_sort function according to the described algorithm above.
'''

def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i -1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums

print(bubble_sort([1, 0, 9, 8, 8, 7]))


