from string import ascii_letters
import unittest

def longest_substring_with_k_distinct(str, k):
  '''
  Iterate through array
    Compute char_right and char_left
    Start with char_right and start sliding right side of window towards the right. Track character occurance in char_freq hash.
    Move to char_left. All char_left will already be accounted for in char_freq. 
      Delete from char_freq is freq is 0, then slide left side of window to right.
      Do this while length of char_freq is greater than k
  When you're done, re-compute max_length as bigger number between itself and difference between win_end and win_start + 1
  '''
  window_start = max_length = 0
  char_freq = {}

  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in char_freq:
      char_freq[right_char] = 0
    char_freq[right_char] += 1

    while len(char_freq) > k:
      left_char = str[window_start]
      char_freq[left_char] -= 1
      if char_freq[left_char] == 0:
        del char_freq[left_char]
      window_start += 1
    
    max_length = max(max_length, window_end - window_start + 1)
  return max_length

def smallest_subarray_with_given_sum(s, arr):
  window_start = window_sum = 0
  min_length = float('inf')

  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    while window_sum >= s:
      min_length = min(min_length, window_end - window_start + 1)
      window_sum -= arr[window_start]
      window_start += 1
  if min_length == float('inf'):
    return 0
  return min_length

def max_sub_array_of_size_k(k, arr):
  '''
  Given an array of positive numbers and a positive
  number k, find the maximum sum of any continuous 
  subarray of size k
  Input: [2, 1, 5, 1, 3, 2], k=3 
  Output: 9
  '''
  window_start = max_window = window_sum = 0
  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    if window_end >= k - 1:
      max_window = max(max_window, window_sum)
      window_sum -= arr[window_start]
      window_start += 1
  return max_window

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

  def test_longest_substring_with_k_distinct(self):
    self.assertEqual(longest_substring_with_k_distinct("araaci", 2), 4)
    self.assertEqual(longest_substring_with_k_distinct("araaci", 1), 2)
    self.assertEqual(longest_substring_with_k_distinct("cbbebi", 3), 5)

  def test_smallest_subarray_with_given_sum(self):
    self.assertEqual(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]), 2)
    self.assertEqual(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]), 1)
    self.assertEqual(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]), 3)

  def test_max_sub_array_of_size_k(self):
    result = max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
    self.assertEqual(result, 9)

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