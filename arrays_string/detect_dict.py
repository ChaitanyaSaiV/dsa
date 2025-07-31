""" detect dictionary
Write a function, detectDictionary, that takes in a dictionary of words and an alphabet string. The function should return a boolean indicating whether or not all words of the dictionary are lexically-ordered according to the alphabet.

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters. """


def detect_dictionary(dictionary, alphabet):
  length = len(dictionary)

  i = 0
  j = 1
  
  while j < length:
    if not lexical_order(dictionary[i], dictionary[j], alphabet):
      return False
    i += 1
    j += 1

  return True


def lexical_order(word_1, word_2, alphabet):
  length = max(len(word_1), len(word_2))

  i = 0

  while i < length:
    if i > len(word_1) - 1:
      word_1_index = float("-inf")
    else:
      word_1_index = alphabet.index(word_1[i])

    if i > len(word_2) - 1:
      word_2_index = float("-inf")
    else:
      word_2_index = alphabet.index(word_2[i])
    i += 1
    if word_1_index > word_2_index:
      return False
    elif word_1_index < word_2_index:
      return True
    else:
      continue


  return True


dictionary = ["miles", "milestone", "pint", "proper", "process","goal", "apple"];
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> False