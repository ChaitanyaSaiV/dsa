def subsets(elements):
  if len(elements) == 0:
    return [[]]

  first_element = elements[0]

  subs_without_first = subsets(elements[1:])

  subs_with_first = []

  for sub in subs_without_first:
    subs_with_first.append([first_element, *sub])

  return subs_with_first + subs_without_first




subsets(['q', 'r', 's', 't']) # ->
# [
#   [],
#   [ 't' ],
#   [ 's' ],
#   [ 's', 't' ],
#   [ 'r' ],
#   [ 'r', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 's', 't' ],
#   [ 'q' ],
#   [ 'q', 't' ],
#   [ 'q', 's' ],
#   [ 'q', 's', 't' ],
#   [ 'q', 'r' ],
#   [ 'q', 'r', 't' ],
#   [ 'q', 'r', 's' ],
#   [ 'q', 'r', 's', 't' ]
# ]