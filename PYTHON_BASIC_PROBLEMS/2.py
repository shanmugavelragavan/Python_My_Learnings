# 2. Write a python function (without using any libraries) to the number of Occurrences of string s1 in input string
# input = "This is a test"
# s1 = "is"
# countStrOccurrences(input,s1) should return the number of occurrences of is.

def occurrences(input, s1):
  count = 0
  end = len(input) - len(s1)
  for i in range(0,end):
    if input[i:i + len(s1)] == s1:
      count += 1
  return count
  
print(occurrences("This is a test", "is"))
