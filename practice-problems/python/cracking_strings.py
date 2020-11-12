'''
1.1
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
'''

test_cases_1_1 = ['abc1frgt', 'abcdefghijklmnop', 'aaaaaa', 'bcdefaaght', 'ythbuioh']

# no external datatypes
def unique_chars(s: str) -> bool:
  for i in range(len(s)):
    for j in range(i + 1, len(s)):
      if s[i] == s[j]: return False
  return True

# print(unique_chars(test_cases_1_1[3]))

def unique_chars_hash(s: str) -> bool:
  table = {}

  for i in range(len(s)):
    if s[i] not in table:
      table[s[i]] = i
    else:
      return False
  return True

# print(unique_chars_hash(test_cases_1_1[1]))

'''
1.2
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.
'''

def check_permutation(s_1: str, s_2: str) -> bool:
  if len(s_1) != len(s_2):
    return False
  # turn strings into sorted arrays 
  s_1 = list(s_1).sort()
  s_2 = list(s_2).sort()
  
  return True if s_1 == s_2 else False 

test_cases_1_2 = ['abcd', 'dcba', 'abcde', 'abch']

# print(check_permutation(test_cases_1_2[0], test_cases_1_2[3]))

'''
1.3 
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
'''

def URLify(s: str) -> str:
  # s.replace(' ', '%20')
  for i in range(len(s)):
    if s[i] == ' ':
      s = s[:i] + '%20' + s[i +1:]
  return s
test_cases_1_3 = ['hello world', 'goodbye cruel world']

# print(URLify(test_cases_1_3[1]))

'''
find all lowercase permutations of a string
'''

def list_to_string(li):
  stringify = ''
  for i in range(len(li)):
    stringify += li[i]
  return stringify

def permutation_list(li: list) -> list:
  if len(li) == 0: return []
  if len(li) == 1: return [li]
  return_li = []
  for i in range(len(li)):
    current = li[i]
    rest = li[:i] + li[i+1:]
    for perm in permutation_list(rest):
      return_li.append([current] + perm)
        
  return return_li 

def string_permutation_table(s: str) -> dict:
  table = {}
  inc = 0
  table[s] = inc
  perms = permutation_list(list(s))
  for perm in perms:
    stringify = list_to_string(perm)
    if stringify not in table:
      table[stringify] = inc
      inc += 1
  return table

# print(string_permutation_table('Tact Coa'))

'''
1.4
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
'''

# print(permutations('Tact Coa'))

def palindrome_check(s: str) -> bool:
  s = s.replace(' ', '')
  rev = s[::-1]
  return True if rev == s else False

# print(palindrome_check('taco cat'))


def palindrome_permutations(s: str) -> list:
  table = string_permutation_table(s)
  palindromes = []

  for permutation in table:
    # print(palindrome_check(permutation))
    if palindrome_check(permutation):
      palindromes.append(permutation)
  return palindromes

# solves with math
def pal_2(s):
  table = {}
  # count chars
  for i in range(len(s)):
    if s[i] not in table:
      table[s[i]] = 1
    else:
      table[s[i]] += 1
  print(table)
  # count the occurances of chars with an odd count
  odds = 0
  for char in table:
    if table[char] % 2 != 0:
      odds += 1
  if len(s) % 2 == 0:
    return True if odds == 0 else False
  else:
    return True if odds == 1 else False
  

# my_pal = pal_2('yeet')

# print(1 % 2)

# print(my_pal)

# li = palindrome_permutations('racecar')

# print(li)

'''
1.5
One Away
There are three types of edits that can be performeded on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit away (or zero).
'''

def one_away(s_1: str, s_2: str) -> bool:
  # case 0 zero edits away
  if s_1 == s_2: 
    print('case 0')
    return True
  
  # case 1 no single edit will make the strings the same
  if len(s_1) > len(s_2) + 1 or len(s_2) > len(s_1) + 1:
    print('case 1')
    return False 

  # case 2 if one character needs to be replaced
  if len(s_1) == len(s_2):
    print('case 2')

    # loop over strings keepning track of the number of differences
    num_differences = 0
    for i in range(len(s_1)):
      if s_1[i] != s_2[i]: num_differences += 1

    # return true if only one difference was found 
    return True if num_differences <= 1 else False

  # listify strings to make them easier to work with
  s_1 = list(s_1)
  s_2 = list(s_2)

  # find longer and shorter string
  longer_string = s_1 if len(s_1) > len(s_2) else s_2
  shorter_string = s_1 if len(s_1) < len(s_2) else s_2

  # case 3 if one character needs to be removed or added
  for i in range(len(longer_string)):
    # splice out the first different character and compare the strings 
    if longer_string[i] != shorter_string[i]:
      # remove the offending character from the longer string
      splice_longer = longer_string[:i] + longer_string[i + 1:]
      # splice the offending character into the shorter string
      splice_shorter = shorter_string[:i] + [longer_string[i]] + shorter_string[i + 1:]
      # make comparisons among the spliced strings
      if splice_longer == shorter_string or splice_shorter == longer_string:
        print('case 3')
        return True 
      else:
        print('case 3')
        return False

  # you shouldn't be here
  return 'oh no!'

# test_cases_1_5 = ['pale', 'ple', 'bake']

# solution = one_away(test_cases_1_5[0], test_cases_1_5[1])
# print(solution)
'''
1.6
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

def string_compression(s: str) -> str:
  # make hash table of character counts
  char_table = {}
  sorted_s = sorted(s)

  for i in range(len(sorted_s)):
    if sorted_s[i] not in char_table: 
      char_table[sorted_s[i]] = 1
    else: 
      char_table[sorted_s[i]] += 1
  
  # make compressed string from table
  compressed_s = ''
  for char in char_table:
    compressed_s = compressed_s + char + str(char_table[char])
  
  return compressed_s if len(compressed_s) < len(s) else s

# solution = string_compression('cbbbbbbbddddegb77777ik')

# print(solution)

'''
1.7
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''

# rotates 180 degrees
# def rotate_matrix(matrix: list) -> list:
#   # reverse each list
#   for i in range(len(matrix)):
#     matrix[i] = matrix[i][::-1]
#   # reverse the matirx 
#   matrix = matrix[::-1]
#   return matrix

# rotates 180 degrees
def rotate_matrix(matrix: list) -> list:
  # reverse each list
  for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]
  # reverse the matirx 
  matrix = matrix[::-1]
  return matrix

matrix = [
  [0, 0, 1, 1],
  [0, 0, 1, 1],
  [2, 2, 3, 3],
  [2, 2, 3, 3]
]

for li in matrix:
  print(li)

solution = rotate_matrix(matrix)

print('solution:')

for li in solution:
  print(li)

'''
1.9
String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
'''

def string_rotation(s_1: str = "waterbottle", s_2: str = "erbottlewat") -> bool:
  # make s_2 into array to rotate it easier
  string_list = list(s_2)

  # rotate the string list, checking each rotation against s_1
  for _ in range(len(string_list)):
    string_list = [string_list.pop()] + string_list
    if ''.join(string_list) == s_1:
      return True

  return False
  
# solution = string_rotation()
# print(solution)