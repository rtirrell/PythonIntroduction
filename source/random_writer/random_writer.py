#!/usr/bin/env python

### 
# Generate 'random writing' based on an input file. It'll seem like the
# writer's style, and be (mostly) syntactically and grammatically correct,
# but semantically meaningless.
###

# Provides access to random.choice, which we use to pick random characters
# from a list of possibilities.
import random

# How many characters to use at one time for determining transitions. Think
# about what varying this would mean - if we chose a very small value, then
# we might see something close to gibberish, because likely at some point in
# the input file we'd observe 'a' followed by just about anything.
# On the other hand, using a much larger value would constrain our choices a
# lot, and we might just end up regenerating the input file.
# If we used value higher than 10 (but not too high), we might observe
# significant portions of the input file (maybe sentence fragments or 
# sentences) reproduced verbatim, but with their relative ordering changed.
ORDER = 15

# How many characters we want to generate (maximum).
OUTPUT_SIZE = 2000

## 
# Warning: this is the hard part! We want to use the most frequently-occurring
# chunk to start the generating process, and this function returns it. Using 
# that will typically generate the best output.
def get_starting_chunk(transitions):
  # Sort the chunks and the characters that follow them by the number of
  # characters that occur after that chunk (i.e., the number of times we see the
  # chunk in the document. Characters can be counted multiple times).
  # We return the first element (the chunk of text) of the last element in our
  # sorted list of pairs - the sort is ascending (smallest to largest count).
  return sorted(
    # transitions.items() converts the dictionary to a list of lists, like:
    # [
    #   [chunk1, [char1, char2, ...]],
    #   [chunk2, [char1, char2, ...]],
    #   [chunk3, [char1, char2, ...]],
    #   ...
    # ]
    #
    # Then the (i, len(j)) bit converts that list to a list of 
    # [chunk, count], like:
    # [[chunk1, count1], [chunk2, count2], [chunk3, count3], ...]
    #
    # Specifically, for each [chunk, list of chars] pair, we create a new pair
    # that is [chunk, len(list of pairs)].
    [(chunk, len(characters)) for chunk, characters in transitions.items()], 

    # This line tells sorted() to sort by the second element - that is, 
    # the count.
    # 
    # lambda is basically a mini-function. We could also write this like:
    # def sort_func(chunk_count_pair):
    #   return chunk_count_pair[1]
    key = lambda chunk_count_pair: chunk_count_pair[1]
  )[-1][0]

##
# Generate gibberish output for the given file.
def generate(filename):
  # Open the file, read all of it (read()), remove any whitespace at the 
  # beginning or end (strip()), and replace newlines with spaces.
  chars = open(filename).read().strip().replace('\n', ' ')

  # This will associate chunks of text with lists of the characters that follow
  # those chunks in the document. In other words - it associates chunks of text
  # with the list of characters they might transition to, as observed in the
  # input file.
  transitions = {}
  
  # Because our chunk is ORDER characters long, and we also want to add the
  # character right after the chunk to that chunk's associated list, we only
  # iterate up to the ORDER + 1th last character (so, for order 10, the last
  # chunk is the 11th to 2nd last characters).
  # 
  # Remember that range doesn't generate the last value it is given - if this
  # is a little unclear, play around with some examples.
  for i in range(len(chars) - ORDER):

    # An ORDER-length chunk of text we are finding transitions for.
    chunk = chars[i:i + ORDER]

    # If this chunk is already in our dict, add a new entry with append
    # (the list method).
    if chunk in transitions:
      transitions[chunk].append(chars[i + ORDER])

    # Otherwise, create a new entry in the dictionary that is a list with 
    # one element.
    else:
      transitions[chunk] = [chars[i + ORDER]]

  # We want to start with the most frequently observed chunk. 
  # get_starting_chunk returns exactly that.
  current_chunk = get_starting_chunk(transitions)

  # Initialize output to be an empty string.
  output = ''

  # Keep going until we've generated OUTPUT_SIZE characters (or until we exit
  # manually).
  while len(output) < OUTPUT_SIZE:

    # If we encounter a chunk we don't have following character(s) for, it must
    # have been from the end of the document. It'll probably take us awhile 
    # to get there in any case, so that's enough for now. We use break to exit
    # the loop.
    if current_chunk not in transitions:
      break

    # Otherwise, add a randomly chosen character to the output. 
    # output += <whatever> is equivalent to output = output + <whatever>, it's
    # just a shortcut for convenience. Many languages offer this.
    output += random.choice(transitions[current_chunk])

    # This is the logical essence of the program. We update the current chunk, 
    # using its last ORDER - 1 plus the chosen transition character. Next time
    # around, when we look in transitions, we'll have a list of characters 
    # frequently following this updated chunk, and will thus pick a next 
    # character that is at least a somewhat reasonable choice in English.
    current_chunk = current_chunk[1:] + output[-1]

  # We'll often have leading or trailing whitespace, so remove that and print.
  print output.strip()

# If this file is being run directly (python random_writer.py), get a file
# from the user and run with it. We could also import random_writer, and then
# call random_writer.generate with another filename as the first argument.
if __name__ == '__main__':
  # Get a filename from the user.
  filename = raw_input('Enter a file to use for gibberish generation: ')
  # Call the main generating function with that filename.
  generate(filename)
