from time import perf_counter
from lib import *
import matplotlib.pyplot as plt
import sys
import math

# list of sort algorithms to call
functions = [
  bubble_sort,
  bubble_sort_recursive,
  insertion_sort,
  insertion_sort_recursive,
  bucket_sort,
  heap_sort,
  merge_sort,
  quick_sort
]

# the data to sort
data = random_ints(10)
# k value for bucket sort
num_buckets = math.floor((len(data) * .5))

# force system to run higher recursive calls
if len(data) >= 1000:
  sys.setrecursionlimit(len(data) + 1)

# print lists in console
verbose = True
# plot the times after completion
plot = False

if verbose: print(f'unsorted list:\n{data}')

start_time = 0
times = []
names = []
for i in range(len(functions)):
  # make new list for each sort
  sort_data = data.copy()
  start_time = perf_counter()
  call = functions[i]
  sort = None

  if call.__name__ == 'bucket_sort':
    sort = call(sort_data, num_buckets)
  else:
    sort = call(sort_data)
  proccess_time = float_to_str(perf_counter() - start_time)

  times.append(float(proccess_time))
  names.append(call.__name__)

  sort_test = 'List is sorted' if is_sorted(sort) else 'List is not sorted'

  print(f'{sort_test} {call.__name__} completed in {proccess_time} seconds')

  if verbose: 
    print(sort)


if plot:
  plt.figure(figsize=(13, 8))
  plt.bar(names, times)
  plt.show()

