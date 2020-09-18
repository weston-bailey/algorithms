import random 
import math
import string

# returns a random list of integers with a specified length
def random_ints(length):
  random_ints = []

  while len(random_ints) < length:
    random_ints.append(random.randrange(0, length, 1))
  
  return random_ints

def random_ints_negetive(length):
  random_ints = []

  while len(random_ints) < length:
    if random.random() > .5:
      random_ints.append(random.randrange(0, length, 1))
    else:
      random_ints.append(random.randrange(0, length, 1) * -1)


  
  return random_ints


# returns a random list of integers with a specified length
# optional arg is how many decimal places
def random_floats(length, *args):
  random_floats = []

  while len(random_floats) < length:
    random_floats.append(random.random() * length)
  
  # format the decimal places if argument is present
  if args:
    for i in range(len(random_floats)):
      random_floats[i] = round(random_floats[i], args[0])

  return random_floats


def random_letters(length):
  random_letters = []

  while len(random_letters) < length:
    random_letters.append(random.choice(string.ascii_letters))
  
  return random_letters