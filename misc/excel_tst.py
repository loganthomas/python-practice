
# Why not pandas?
# If must do it this way, better to use "with"
fh = open('excel_test.csv')

position = list()
number = list()
for line in fh:
    line = line.rstrip()
    # print line
    if line.startswith('position'):
        continue
    elements = line.split(',')
    print('Position: ', elements[0], 'Number: ', elements[1])
    position.append(float(elements[0]))
    number.append(float(elements[1]))


print('Sum of Number', sum(number))
print('Number of Records', len(position))
print('Average: ', sum(number) / len(position))







