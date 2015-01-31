#!/usr/bin/python

def count_characters_in_string(string):
  counter = {}

  for c in string:
    #Look for existing character in the counter dict.
    if c in counter:
      #If it exists, increment the char in the dict
      counter[c] = counter[c] + 1
    else:
      #If not, add it to the dict with 1
      counter[c] = 1

  return counter
#end function

# Main Logic
default = "This is an example string that is used for testing purposes."
result = count_characters_in_string(default)

print "Here is the collection of characters for the string: {}".format(default)
print result
