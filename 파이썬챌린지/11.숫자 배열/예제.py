from array import *

nums = array('i', [45, 324, 654, 45, 264])
print(nums)
for x in nums:
    print(x)
numValue = int(input("Enter number: "))
nums.append(numValue)
print(nums)
nums.reverse()
print(nums)
nums = sorted(nums)
print(nums)
nums.pop()
print(nums)
newArray = array('i', [])
more = int(input("How many items: "))
for y in range(0, more):
    numValue = int(input("Enter number: "))
    newArray.append(numValue)
nums.extend(newArray)
print(nums)
getRid = int(input("Enter item index: "))
nums.remove(getRid)
print(nums)
print(f"num array have {nums.count(45)} of 45")
