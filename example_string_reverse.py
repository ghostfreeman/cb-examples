#!/usr/bin/python

str = "Hello"
newList = [ ]
reversedStr = ""

# Because we can't use "native string manipulation" we will throw everything in
# A list using a for loop
for c in str:
  newList.append(c)

# Because I don't want to get in trouble over the native options provided in
# List objects, we will pop it iteratively until its empty and exit gracefully
sizeOfList = len(newList)
currentItem = sizeOfList

while currentItem != 0:
  reversedStr += newList[currentItem-1];
  currentItem = currentItem - 1

# Output results
print "The reversed string of Hello is:"
print reversedStr
