# 3. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

list1 = ['aba','121','kgf','abc']

def words(a):
  b = 0

  for word in a:
    if len(word) > 1 and word[0] == word[-1]:
      b+= 1
  return b

print(words(list1))