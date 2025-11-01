def two_sum(list, target):
    dict = {}
    for i, x in enumerate(list):
        num = target - x
        if num not in dict:
            dict[num] 
        