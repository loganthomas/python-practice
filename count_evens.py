#Return the number of even ints in the given array

def count_evens(nums):
    count=0
    for a in nums:
        if a % 2==0:
            count=count+1
    return count

integers=list()
inputs = raw_input("Please enter integer list seperated by a comma:")
numbers = inputs.split(',')
for x in numbers:
    x=int(x)
    integers.append(x)
print integers

evens = count_evens(integers)
print "Number of even integers:",evens