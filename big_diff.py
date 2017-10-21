#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.

def big_diff(nums):
    m=max(nums)
    v=min(nums)
    diff = m-v
    return diff

integers=list()
inputs = raw_input("Please enter a list of integers seperated by a comma:")
numbers = inputs.split(",")
for x in numbers:
    x=int(x)
    integers.append(x)
print integers
if len(integers)<=1:
    print "Please enter a list of more than 1 integers"
    exit()

diff = big_diff(integers)
print "Difference:", diff
