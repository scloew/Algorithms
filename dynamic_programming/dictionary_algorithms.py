from collections import Counter


def first_non_recurring_char(string_):
  count_ = Counter(string_)
  for key, val in count_.items():
    if val == 1:
      return key
  return None


if __name__ == '__main__':
  print(first_non_recurring_char('aabcc'))
  print(first_non_recurring_char('abcdabce'))
  print(first_non_recurring_char('aaabbbccc'))
  print(first_non_recurring_char(''))
