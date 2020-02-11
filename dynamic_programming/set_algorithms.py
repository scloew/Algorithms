def word_breaking(words_set, string_):
  """
  :param words_set: set of words to search for
  :param string_: string to see if can be segmented into
  :return: set of words that can be generated from
  """
  string_set = set([string_[i:j+i] for i in range(len(string_)) for j in range(i, len(string_)+1)])
  print(string_set)
  return words_set.intersection(string_set)


if __name__ == '__main__':
  print(word_breaking({'a', 'b', 'c', 'd', 'abc'}, 'abc'))
  print(word_breaking({'hello world', 'hello', 'world', 'foo', 'o w'}, 'hello world'))
