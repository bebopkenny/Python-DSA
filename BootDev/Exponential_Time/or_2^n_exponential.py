'''
Order 2^N - Exponential

O(2^n) is the first Big O class that we've dealt with that falls into the scary exponential category of algorithms.

Algorithms that grow at an exponential rate become impossible to compute after so few iterations that they are almost worthless in practicality.
Assignment

At LockedIn, we need to be able to compute the power set of a set of influencers. It has something to do with targeting segments of an audience with ads. I don't know, I just work here.

A power set consists of all possible combinations of elements in a given collection. For example, the power set of {1, 2, 3} is:

{
  {},
  {1},
  {2},
  {3},
  {1, 2},
  {1, 3},
  {2, 3},
  {1, 2, 3},
}

We'll work with Python lists instead of sets for simplicity.

    An empty set will just be an empty list: [].

Complete the power_set function using the following algorithm:

    Check if the input list is empty. If it is, return a list containing an empty list. (The power set of an empty collection contains just the empty set)
    Otherwise, create a list that contains an empty list. This will hold the final collection of subsets (let's call it 'subsets').
    For each element in the input list:
        Create a new empty list. This will hold the new subsets that include the current element.
        Iterate over each subset in your main collection ('subsets'):
            Create a new subset by adding the current element to the existing subset.
            Append this new subset to the list of new subsets.
        Extend the main collection of subsets with your newly created subsets.
    Return the final collection of subsets.

Observe!

Notice how the power_set() output gets exponentially larger with each iteration because its complexity class is O(2^n).

If we could calculate one subset per millisecond, completing the power_set() of just 25 items would take approximately 9 hours, and that's not accounting for the massive amounts of memory we would need. 40 items would take over 34 years!
'''
def power_set(input_set):
    if not input_set:
        return [[]]
    subsets = []
    first = input_set[0]
    remining = input_set[1:]
    remaning_subsets = power_set(remaining)
    for i in remaining_sebset:
        subsets.append([first] + subset)
        subsets.append(subset)
    return subset

'''
Exponential Growth Sequences

At LockedIn, we are interested in simulating the exponential growth of an influencer's followers over a certain period with an adjustable growth factor.
Assignment

Complete the exponential_growth function. Given the initial followers count n, growth factor factor, and number of days days, return a list containing the exponential growth of followers for each day.

For example:

- Initial followers: 10
- Growth factor: 2
- Days: 4

Growth sequence: [10, 20, 40, 80, 160]
'''

def exponential_growth(n, factor, days):
    empty = []
    empty.append(n)
    i = 0
    while i < days:
        n *= 2
        empty.append(n)
        i += 1
    return print(empty)

exponential_growth(10, 2, 4)
















