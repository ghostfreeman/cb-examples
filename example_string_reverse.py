#!/usr/bin/python

# Function
def reverse_string(string):
  newList = [ ]
  reversedStr = ""

  # Because we can't use "native string manipulation" we will throw everything in
  # A list using a for loop
  for c in string:
    newList.append(c)

  # Because I don't want to get in trouble over the native options provided in
  # List objects, we will pop it iteratively until its empty and exit gracefully
  sizeOfList = len(newList)
  currentItem = sizeOfList

  while currentItem != 0:
    reversedStr += newList[currentItem-1];
    currentItem = currentItem - 1

  # Output results
  return reversedStr
#End function

str = "Hello"

print "The reverse of the string Hello is:"
print reverse_string(str)
