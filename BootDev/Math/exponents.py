'''
Exponents

I promise we'll get to how this relates to coding, but first we need to review some math stuff.

An exponent indicates how many times a number is to be multiplied by itself.

For example:

53 = 5 * 5 * 5 = 125

Sometimes exponents are also written using the caret symbol (^):

5^3 = 53
Exponent Syntax

The ** operator calculates an exponent in Python. (Why not the ^ operator? Blame Fortran.)

square = 2 ** 2
# square = 4

cube = 2 ** 3
# cube = 8

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Exponents and power operator

Assignment

In the social media industry, there is a concept called "spread": how much a post spreads due to "reshares" after all of the original author's followers see it. As it turns out, social media posts spread at an exponential rate! We've found that the estimated spread of a post can be calculated with this formula:

estimated_spread = average_audience_followers * ( num_followers ^ 1.2 )

In the formula above, average_audience_followers is an average calculated from each number within the audiences_followers argument - which is a list containing the individual follower counts of the author's followers. For example, if audiences_followers = [2, 3, 2, 19], then:

    - the author has 4 total followers
    - each follower has their own 2, 3, 2, and 19 followers, respectively.

Complete the get_estimated_spread function by implementing the formula above. The only input is audiences_followers, which is a list of the follower counts of all the followers the author has. Return the estimated spread. If the audiences_followers list is empty, return 0.
'''

def get_estimated_spread(audiences_followers):
    if not audiences_followers:
        return 0
    total_followers = len(audiences_followers)
    sum = 0
    for i in audiences_followers:
        sum += i
    average = sum / total_followers
    result = average * (total_followers**1.2)
    print(result)
    return result

input = [12, 12, 12]

get_estimated_spread(input)