'''
Problem 5: Merge Performance Schedules

You are organizing a cultural festival and have two performance schedules, schedule1 and schedule2, each represented by a string where each character corresponds to a performance slot. Merge the schedules by adding performances in alternating order, starting with schedule1. If one schedule is longer than the other, append the additional performances onto the end of the merged schedule.

Return the merged performance schedule.
'''

def merge_schedules(schedule1, schedule2):
    right = 0
    left = 0
    string = ""
    while right >= left:
        print(f"SCH RIGHT: {schedule1[right]}")
        string += schedule1[right]
        right += 1
        print(f"SCH LEFT: {schedule2[left]}")
        string += schedule2[left]
        left += 1
        print(string)
    return string

# Example Usage:

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 

# Example Output:

# apbqcr
# apbqrs
# apbqcd
