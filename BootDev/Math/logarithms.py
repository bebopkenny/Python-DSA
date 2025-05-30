import math
'''
Logarithms

A logarithm is the inverse of an exponent.

24 = 16

log216 = 4

"log216" can be read as "log base 2 of 16", and means "the number of times 2 must be multiplied by itself to equal 16".

"log216" might also be written as log2(16)

Some more examples:
Logarithm 	Result
log22 	    1
log24 	    2
log28 	    3
log216 	    4
log1010 	1
log10100 	2
log101000 	3
log1010000 	4

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: What is a logarithm

Python Syntax

There isn't a language-level operator to calculate a logarithm, but we can import the math library and use the math.log() function.

import math

print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")
# Logarithm base 2 of 16 is: 4.0

Assignment

Let's create an "influencer score". It will be a small number (like less than 100) that will give influencers a metric for comparing their social media success against their peers.

Complete the get_influencer_score function. An influencer score is their average engagement percentage multiplied by log base 2 of their follower count.
'''

def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2) # log base 2 of their follower total amount