numBottles = 12
numExchange = 4
res = numBottles
left = 0
while numBottles >= numExchange:
    left = numBottles % numExchange
    numBottles //= numExchange # exchange for new bottles
    res += numBottles
    numBottles += left

print(res)