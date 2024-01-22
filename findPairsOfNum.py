lst = [2,7,11,15,12,-4,-6]
target = 9 
def findPairs(lst,target):
    results=[]
    while lst:
        i = lst.pop()
        diff = target - i 
        if diff in lst:
            results.append((diff,i))
    results.reverse()
    return results
print(findPairs(lst,target))