def insertion_sort(unsorted_list):
  # iterate through list and move elements down if they are less than the element to the left
  for i in range(len(unsorted_list)):
    j = i
    while j > 0 and unsorted_list[j] < unsorted_list[j - 1]:
      unsorted_list[j - 1], unsorted_list[j] = unsorted_list[j], unsorted_list[j - 1]
      j = j - 1

  return unsorted_list 

# not working
def insertion_sort_recursive(unsorted_list, *args):
  index = None

  # if a second argument is present, assign it to index
  if args:
    index = args[0]
  else: 
    index = len(unsorted_list) - 1

  # base case 
  if index == 0: 
    return unsorted_list 

  # move elements down the list if they are less than the element to the left
  j = index
  print(unsorted_list[j - 1])
  print(unsorted_list[j], unsorted_list[j - 1], unsorted_list[j] > unsorted_list[j - 1])
  print(unsorted_list)
  while j > 0 and unsorted_list[j] > unsorted_list[j - 1]:
    unsorted_list[j - 1], unsorted_list[j] = unsorted_list[j], unsorted_list[j - 1]
    j = j - 1

  return insertion_sort_recursive(unsorted_list, index - 1)
  






