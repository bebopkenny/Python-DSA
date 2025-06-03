'''
Reduction to P

Let's take an exponential time algorithm and fix it up so it can run in polynomial time!

The Fibonacci sequence is a sequence of numbers where each number is the sum of the two numbers before it. Like this:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

We want a function that, given an index in the sequence, returns the Fibonacci number at that index. For example:

    fib(0) -> 0
    fib(1) -> 1
    fib(2) -> 1
    fib(3) -> 2
    fib(4) -> 3
    fib(5) -> 5
    fib(6) -> 8
    fib(7) -> 13

Here are the implementation details to do it in polynomial time:

    The input n represents the index of the desired Fibonacci number.
    Initialize three variables: grandparent = 0, parent = 1, and a placeholder current to store the new Fibonacci number at each step.
    Write a loop that iterates n - 1 times. (For example, if n = 2, no iterations occur.)
    Inside the loop:
        Set current = parent + grandparent
        Adjust the ancestor values (parent and grandparent) to maintain the sequence.
    Once the loop completes, return current.

Assignment

Our data scientists at LockedIn have found that the growth of the average influencer's follow count is roughly the same growth rate as the Fibonacci sequence! In other words, after 6 weeks of good social media posts, the average influencer will have 8 followers. After 7 weeks, 13 followers, and so on.

The trouble is, our current implementation of the fib function takes so long (exponential time!) to complete that when our influencers navigate to their analytics page it often never completes loading!

Adjust the fib function using the given algorithm to achieve polynomial runtime.
'''

# Starter code
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Refactor code
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    grandparent = 0 # two before
    parent = 1 # one before
    current = None
    for i in range(n - 1):
        current = parent + grandparent
        grandparent = parent # move to the next step
        parent = current # gets current
    return current
        









