#!/usr/bin/env python
import random

# How many characters to use at one time for determining transitions.
ORDER = 10
# How many characters we want to print.
OUTPUT_SIZE = 2000

def get_starting_chunk(transitions):
  # Sort the chunks and the characters that follow them by the number of
  # characters that occur after that chunk (i.e., the number of times we see the
  # chunk in the document. Characters can be counted multiple times).
  # transitions.items() converts the dictionary to a list of pairs of
  # (chunk, [char1, char2, ...]), and the (i, len(j)) bit converts that list to
  # a list of (chunk, count).
  return sorted(
    [(i, len(j)) for i, j in transitions.items()], 
    # This line tells sorted() to sort by the second element - that is, the count.
    key = lambda v: v[1]
  )[-1][0]

def generate():
# Get a filename from the user.
  filename = raw_input('Enter a file to use for gibberish generation: ')
# Open the file, read all of it, remove any whitespace at the beginning or end,
# and replace newlines with spaces.
  chars = open(filename).read().strip().replace('\n', ' ')

  transitions = {}
  for i in range(len(chars) - ORDER):
    # The chunk of characters we are finding transitions for.
    chunk = chars[i:i + ORDER]
    # If this is already in our dict, add a new entry with append (a list method).
    if chunk in transitions:
      transitions[chunk].append(chars[i + ORDER])
    # Otherwise, create a new entry in the dictionary that is a list with one element.
    else:
      transitions[chunk] = [chars[i + ORDER]]

# We want to start with the most frequently observed chunk, which will be last
# in the sorting. Since the elements of chunk_counts are [chunk, count] pairs,
# we take the first element.
  current_chunk = get_starting_chunk(transitions)

# Initialize output to be an empty string.
  output = ''
  while len(output) < OUTPUT_SIZE:
    # If we encounter a chunk we don't have following character(s) for, it must
    # have occurred at the end of the document. That's enough for now, and we use
    # break to exit the loop.
    if current_chunk not in transitions:
      break
    # Otherwise, add a randomly chosen character to the output.
    output += random.choice(transitions[current_chunk])
    # And update the current chunk.
    current_chunk = current_chunk[1:] + output[-1]

# We'll often have leading or trailing whitespace, so remove that and print.
  print output.strip()

if __name__ == '__main__':
  generate()
