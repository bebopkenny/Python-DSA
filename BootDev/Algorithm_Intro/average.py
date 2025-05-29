'''
Average

We now need a way to show our LockedIn influencers the average follower count of the people they follow. This will help them know if they're following people who are more or less popular than them.
Assignment

Complete the average_followers function. It should return the average of the given list of numbers.
'''

def average(nums):
    if not nums: # if nums is empty, return None
        return None
    total = len(nums) # get total of nums
    sum = 0 
    for i in nums:
        sum += i # add each element to the sum
    return (sum / total) # calculate the average 
