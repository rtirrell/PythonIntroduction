# Regular expressions could be the subject of an entire course in their own
# right. We just want to be able to split our lines on whitespace, which
# could mean (one or more) spaces, tabs, newlines and so forth.
import re

# Allows access to command-line arguments.
import sys

# Provides an implementation of the Porter stemming algorithm, which attempts
# to break words to their base or root form (in a process known as stemming).
import Porter

stemmer = Porter.PorterStemmer()

counts = {}

# Read all of the text, and convert it to lowercase - we want to examine word
# duplication independent of case.
text = open(sys.argv[1]).read().lower()

# Replace every character that is not a letter, number or whitespace with a
# space. The '^' negates the ranges that follow it.
alphanumeric_text = re.sub('[^A-Za-z0-9]', ' ', text)

# Split words by whitespace character. Because Python interprets backspaces as
# special characters (e.g., '\t' represents a tab and '\n' a newline), we have
# to add an extra backslash to indicate we literally mean backslash + s.
words = re.split('\\s+', alphanumeric_text.strip())

for word in words:
  # Ignore blanks and short words.
  if len(word) == 0 or len(word) < 5:
    continue
  
  stemmed_word = stemmer.stem_simple(word)
  
  # If we have seen this stemmed word before, add one to that count.
  if stemmed_word in counts:
    counts[stemmed_word] += 1
  # Otherwise, insert a new word into the dictionary with a starting count of 1.
  else:
    counts[stemmed_word] = 1
  
print counts