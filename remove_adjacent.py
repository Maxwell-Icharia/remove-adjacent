def remove_adjacent(nums):
  new_list = []
  nums.sort()
  for x in nums:
    if x not in new_list:
      new_list.append(x)
  return new_list