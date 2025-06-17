'''

Problem 4: Engagement Boost

You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Your Task:

    Read through the existing solution and add comments so that everyone in your pod understands how it works.
    Modify the solution below to use the two-pointer technique.
'''

def engagement_boost(engagements): 
    stack = []
    left = 0
    right = len(engagements) - 1
    while left <= right:
        if abs(engagements[left]) < abs(engagements[right]):
            stack.append(engagements[left] ** 2)
            left += 1
        else:
            stack.append(engagements[right] ** 2)
            right -= 1
    stack.reverse()
    return stack

# Example Usage:

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

# Example Output:

# [0, 1, 9, 16, 100]
# [4, 9, 9, 49, 121]

