import numpy
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print(sorted(ages)) #sorted list

#adding min and max numbers to the ages list
ages.append(min(ages))
ages.append(max(ages))
print(ages)

#median of the ages list
print(numpy.median(ages))

#average of the ages list.
print(numpy.average(ages))

#range of the list
print(max(ages)-min(ages))