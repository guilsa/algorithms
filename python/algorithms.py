from string import ascii_letters
import unittest

def find_averages_of_subarrays(k, array):
  '''
  o(n) linear time
  '''
  result = []
  window_start, window_sum = 0, 0.0
  for window_end in range(len(array)):
    window_sum += array[window_end]
    if window_end >= k - 1:
      result.append(window_sum / k)
      window_sum -= array[window_start]
      window_start += 1
  return result

def merge_sort(list):

  if len(list) > 1:
    mid = len(list) // 2
    L = list[:mid]
    R = list[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        list[k] = L[i]
        i += 1
      else:
        list[k] = R[j]
        j += 1
      k += 1

    while i < len(L):
      list[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      list[k] = R[j]
      j += 1 
      k += 1
  
  return list

def insertion_sort(list):
  for i in range(len(list)):
    current_value = list[i]
    pos = i
    while list[pos - 1] > current_value and pos > 0:
      list[pos] = list[pos - 1]
      pos -= 1
    list[pos] = current_value

  return list

def is_palindrome(s):
  '''
  A man, a plan, a canal: Panama

  1. lowercase everything
  2. remove anything that isnt a letter, including spaces
  3. if len is odd, find the middle and remove 
  4. check n and n - 1, loop until middle
  5. for every iteration, if n != n - 1 return false
  '''
  
  i = 0
  j = len(s) - 1
  while i < j:
    while i < j and not s[i].isalnum():
      i += 1
    while i < j and not s[j].isalnum():
      j -= 1
    if s[i].lower() != s[j].lower():
      return False
    i, j = i + 1, j - 1  
  return True


class Test(unittest.TestCase):

  def test_find_averages_of_subarrays(self):
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    self.assertEqual(result, [2.2, 2.8, 2.4, 3.6, 2.8])

  def test_merge_sort(self):
    self.assertEqual(merge_sort([8,4,3,5]), [3,4,5,8])

  def test_insertion_sort(self):
    self.assertEqual(insertion_sort([8, 0, 6, 3]), [0, 3, 6, 8])

  def test_is_palindrome(self):
    self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))
 


if __name__ == '__main__':
  unittest.main()