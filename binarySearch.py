import random
import time

#pasa por cada elemento en una lista
def naiveSearch(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

#ocupa que sea una lista ordenada
def binarySearch(list, target, subLim=None, supLim=None):
    if subLim is None:
        subLim = 0
    if supLim is None:
        supLim = len(list)-1
    
    if supLim < subLim:
        return -1
    
    mid = (subLim + supLim) // 2
    
    if list[mid] == target:
        return mid
    elif target < list[mid]:
        return binarySearch(list, target, subLim, mid-1)
    else:
        return binarySearch(list, target, mid+1, supLim)
    
  
#haciendo la lista    
size = 10000
startingCon = set()
while len(startingCon) < size:
    startingCon.add(random.randint(-3*size, 3*size))
orderedlist = sorted(list(startingCon))

#tiempo con el naive search
start = time.time()
for target in orderedlist:
    naiveSearch(orderedlist,target)
end = time.time()
print(f"Tiempo de busqueda ingenua: {end - start} segundos.")

#tiempo con binary search
start = time.time()
for target in orderedlist:
    binarySearch(orderedlist,target)
end = time.time()
print(f"Tiempo de busqueda binaria: {end - start} segundos.")