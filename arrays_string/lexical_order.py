""" lexical order
Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument. The function should return True if the first word should appear before the second word if lexically-ordered according to the given alphabet order. If the second word should appear first, then return False.

Note that the alphabet string may be any arbitrary string.

Intuitively, Lexical Order is like "dictionary" order:

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters. """



def lexical_order(word_1, word_2, alphabet):
  i = 0

  word_1_length = len(word_1) - 1
  word_2_length = len(word_2) - 1

  while i <= word_1_length and i <= word_2_length:
    word_1_current_char = word_1[i]
    word_2_current_char = word_2[i]

    word_1_current_char_rank = alphabet.index(word_1_current_char)
    word_2_current_char_rank = alphabet.index(word_2_current_char)

    i += 1

    if word_1_current_char_rank < word_2_current_char_rank:
      return True
    elif word_1_current_char_rank == word_2_current_char_rank:
      continue
    else:
      return False
  
  return True



alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("backs", "backdoor", alphabet) # -> False