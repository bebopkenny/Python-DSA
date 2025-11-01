def water(items):
    i = 0
    j = len(items) - 1
    max_area = 0
    while i < j:
        temp = min(items[i], items[j])
        max_area = max(max_area, temp * (j - i))
        if items[i] < items[j]:
            i += 1
        elif items[i] > items[j]:
            j -= 1
        else:
            i += 1
        
        
    return max_area


num = [7, 1, 2, 3, 9]

print(water(num))

