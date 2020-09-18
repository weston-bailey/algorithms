def insertion_sort(unsorted_list):
  # iterate through list and move elements down if they are less than the element to the left
  for i in range(len(unsorted_list)):
    j = i
    while j > 0 and unsorted_list[j] < unsorted_list[j - 1]:
      unsorted_list[j - 1], unsorted_list[j] = unsorted_list[j], unsorted_list[j - 1]
      j = j - 1

  return unsorted_list 

# not working
def insertion_sort_recursive(unsorted_list):

  for i in range(len(unsorted_list)):
    sort_recursive(unsorted_list, i)
  
  return unsorted_list
  
def sort_recursive(unsorted_list, index):
  # base case
  if index <= 0:
    return unsorted_list
  if unsorted_list[index] < unsorted_list[index - 1]:
    unsorted_list[index - 1], unsorted_list[index] = unsorted_list[index], unsorted_list[index - 1]
    return sort_recursive(unsorted_list, index - 1)





