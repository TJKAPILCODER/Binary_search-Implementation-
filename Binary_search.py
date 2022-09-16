def binary_search(list, target):
    # Step 1: point to beginning and end of array
    first = 0
    last = len(list) - 1
    
    # step 2: Keep excecuting loop while the value of first is less than or equal to the value of last
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
            
    return None
    
def verify(index):
    if index is not None:
        print("Target found at",index)
    else:
        print("Target Not Found!")
        
result1 = binary_search([1,2,3,4,5,6,7,8,9, 10], 12)
result2 = binary_search([1,2,3,4,5,6,7,8,9, 10], 7)

verify(result1)
verify(result2)
        
    
