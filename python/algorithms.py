from string import ascii_letters
import unittest

def find_word_concatenation(s, words):
  '''
  Given a string and a list of words, find all the starting indices of
  substrings in the given string that are a concatenation of all the
  given words exactly once without any overlapping of words. It is given
  that all words are of the same length.

  Input: String="catfoxcat", Words=["cat", "fox"]
  Output: [0, 3]
  Explanation: The two substring containing both the words are "catfox"
  & "foxcat".

  Strategy:
  first loop -> grows window
  second loop -> compute next word, increment markers, search solution
  third loop -> shrinks window
  '''

  def build_word_count(words):
    count = {}
    for word in words:
      if word not in count:
        count[word] = 0
      count[word] +=1
    return count

  if not words or not s:
    return []

  word_count = build_word_count(words)
  word_len = len(words[0])
  word_count_len = sum(word_count.values())
  output = []

  for i in range(word_len):
    s_count = {}
    left = i
    s_count_len = 0
    
    for j in range(i, len(s), word_len):
      word = s[j:j + word_len]
      if word not in s_count:
        s_count[word] = 0
      s_count[word] += 1
      s_count_len += 1
      
      while s_count_len > word_count_len:
        s_count[s[left:left + word_len]] -= 1
        s_count_len -= 1
        if s_count[s[left:left + word_len]] == 0:
          s_count.pop(s[left:left + word_len])
        left += word_len
      if s_count == word_count:
        output.append(left)

  return output

def non_repeat_substring(s):
  '''
  Given a string, find the length of the longest substring which has no
  repeating characters.
  Input: String="aabccbb"
  Output: 3
  Explanation: The longest substring without any repeating characters is
  "abc".

  This problem is a great example of how the sliding window strategy is
  growing. Here we move `window_start` forward with a `char_index_map`
  as a dict. Non-repeat property means move `window_start` forward if
  char is in `char_index_map`. Then `window_start` must equal to the max
  between `window_start` and `char_index_map[right_char] + 1`. Then we
  finally save right_char's position with `char_index_map[right_char]
  = window_end`. This problem is also the first time we use the `max()`
  function 2X. 

  This is the first time that we use a hash to track the location of a
  char on a string. Notice that the hash holds 2 properties:
    a) the `if right_char not in char_index_map`, which gives us the
       ability to find the "non-repeat" characteristic within our
       substring (our while loop condition). It's the first time we use
       a hash to drive while condition and move `window_start` forward.
    b) the `char_index_map[right_char]`, which gives us its location.
  '''
  pass

def fruits_into_basket(fruits):
  '''
  Given an array of characters where each character represents a
  fruit tree, you are given two baskets and your goal is to put
  maximum number of fruits in each basket. The only restriction is
  that each basket can have only one type of fruit.

  You can start with any tree, but once you have started you can't
  skip a tree. You will pick one fruit from each tree until you
  cannot, i.e., you will stop when you have to pick from a third
  fruit type.

  Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
  Output: 5
  Explanation: We can put 3 'B' in one basket and two 'C' in the
  other basket. This can be done if we start with the second
  letter: ['B', 'C', 'B', 'B', 'C']
  '''
  window_start = max_length = 0
  basket = {}
  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]
    if right_fruit not in basket:
      basket[right_fruit] = 0
    basket[right_fruit] += 1
    while len(basket) > 2:
      left_fruit = fruits[window_start]
      basket[left_fruit] -= 1
      if basket[left_fruit] == 0:
        del basket[left_fruit]
      window_start += 1
    max_length = max(max_length, window_end - window_start + 1)
  return max_length

def longest_substring_with_k_distinct(string, k):
  '''
  Given a string, find the length of the longest substring in it with no
  more than K distinct characters.
  Input: String="araaci", K=2
  Output: 4
  Explanation: The longest substring with no more than '2' distinct 
  characters is "araa".
  
  - Iterate through array
    - Compute char_right and char_left
    - Start with char_right and start sliding right side of window
    towards the right. Track character occurance in char_freq hash.
    - Move to char_left. All char_left will already be accounted for in
    char_freq.
      - Delete from char_freq is freq is 0, then slide left side of
      window to right.
      - Do this while length of char_freq is greater than k
  - When you're done, re-compute max_length as bigger number between
  itself and difference between win_end and win_start + 1
  '''
  window_start = max_length = 0
  char_freq = {}

  for window_end in range(len(string)):
    right_char = string[window_end]
    if right_char not in char_freq:
      char_freq[right_char] = 0
    char_freq[right_char] += 1

    while len(char_freq) > k:
      left_char = string[window_start]
      char_freq[left_char] -= 1
      if char_freq[left_char] == 0:
        del char_freq[left_char]
      window_start += 1
    
    max_length = max(max_length, window_end - window_start + 1)
  return max_length

def smallest_subarray_with_given_sum(s, arr):
  '''
  Find the length of the smallest contiguous subarray whose sum 
  is greater than or equal to `S`. Return 0, if no such subarray 
  exists.
  Input: [2, 1, 5, 2, 3, 2], S=7 
  Output: 2

  Insight: 
    If you forget what to do in the while loop, list out all 
    available variables and try to apply common sense and 
    pick what applies. For ex, it makes sense to do something 
    with window_sum. `Window_sum` and `s` go hand in hand. 
    From then on, introducing a while loop makes the most 
    sense, since we're ensuring we move window_start 
    to left most position before continuing to move window_end.
  '''

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

def get_number_of_islands(grid):
  '''
  Given a 2D array binaryMatrix of 0s and 1s, implement a 
  function getNumberOfIslands that returns the number of 
  islands of 1s in binaryMatrix.
  '''
  def countIslands(i, j, rows, cols, grid):
    stack = []
    stack.append([i, j])
    while stack:
      x, y = stack.pop()
      if grid[x][y] == 1:
        grid[x][y] = -1
        pushIfValid(x + 1, y, rows, cols, stack)
        pushIfValid(x - 1, y, rows, cols, stack)
        pushIfValid(x, y + 1, rows, cols, stack)
        pushIfValid(x, y - 1, rows, cols, stack)

  def pushIfValid(x, y, rows, cols, stack):
    if (x >= 0 and x < rows and y >= 0 and y < cols):
      stack.append([x, y])

  rows = len(grid)
  cols = len(grid[0])
  islands = 0
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 1:
        countIslands(i, j, rows, cols, grid)
        islands += 1
  return islands

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

  def test_find_word_concatenation(self):
    self.assertEqual(
      find_word_concatenation(
        'zackzackbethzack', ['zack', 'beth']
      ), [4, 8]
    )

  def test_fruits_into_basket(self):
    self.assertEqual(fruits_into_basket(['A', 'B', 'C', 'A', 'C']), 3)
    self.assertEqual(fruits_into_basket(['A', 'B', 'C', 'B', 'B', 'C']), 5)

  def test_longest_substring_with_k_distinct(self):
    self.assertEqual(longest_substring_with_k_distinct('araaci', 2), 4)
    self.assertEqual(longest_substring_with_k_distinct('araaci', 1), 2)
    self.assertEqual(longest_substring_with_k_distinct('cbbebi', 3), 5)

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

  def test_get_number_of_islands(self):
    grid = [
      [0, 1, 0, 1, 0],
      [0, 0, 1, 1, 1],
      [1, 0, 0, 1, 0],
      [0, 1, 1, 0, 0],
      [1, 0, 1, 0, 1]
    ]
    grid2 = [
      [1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 1, 1]
    ]
    self.assertEqual(get_number_of_islands(grid), 6)
    self.assertEqual(get_number_of_islands(grid2), 3)

  def test_insertion_sort(self):
    self.assertEqual(insertion_sort([8, 0, 6, 3]), [0, 3, 6, 8])

  def test_is_palindrome(self):
    self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))
 


if __name__ == '__main__':
  unittest.main()