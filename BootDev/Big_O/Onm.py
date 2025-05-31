'''
O(nm)

O(nm) is very similar to O(n^2), but instead of a single input that we care about, there are two. If n and m increase at the same rate, then O(nm) is effectively the same as O(n^2). However, if n or m increases faster or slower, then it's useful to track their complexity separately.
Assignment

LockedIn needs a new tool that allows big brands to see how many of an influencer's followers are loyal to their brand. Complete the get_avg_brand_followers function. It takes two inputs:

    all_handles: a 2-dimensional list, or "list of lists" of strings representing user handles on a per-influencer basis.
    brand_name: a string.

get_avg_brand_followers returns the average number of handles that contain the brand_name across all the lists. Each list represents the audience of a single influencer.
Example Input/Output

Input:

all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name = "cosmo"

Expected output: 1.33 (handles per influencer, because 4 handles contained "cosmo" and there are 3 lists)
Observe

Regarding Big O, the number of influencers (the number of lists) matters. That's our n. However, the average number of followers of each influencer (the average length of the lists) is just as important. That's our m.
'''
def get_avg_brand_followers(all_handles, brand_name):
    counter = 0 # keeping track of the elements that have "brand_name"
    total_counter = 0 # total amount of lists
    for i in all_handles:
        total_counter += 1 # increase after each list 
        for x in i: # loop through each element in each list
            if brand_name in x: # if the word is in the element
                counter += 1 # count how many times it shows up 
    return counter / total_counter # give us the average 
