# 1. Given a array of integers, count of number of occurrences of the maximum element in the array
# Sample Input: 3 2 1 3
# Sample Output: 2

def count_max(arr):
  if not arr:
    return 0
  max_value = max(arr)
  count = arr.count(max_value)
  return count

arr = [3, 2, 1, 3]
count_max(arr)



























































def count_max(arr):
  if not arr:
    return 0
  max_value = max (arr)
  count = arr.count(max_value)
  return count

arr = [3, 2, 1, 3]
result = count_max(arr)
print(result)