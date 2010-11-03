# Import module containing alphabets for the rot13 function.
import string

def rot13(s):
  # Variable to hold the ciphertext.
  new_s = ""

  # Iterate over each letter in the string we want to encrypt.
  for letter in s:

    # Determine which alphabet we should use for encryption.
    if letter in string.ascii_uppercase:
      alphabet = string.ascii_uppercase

    elif letter in string.ascii_lowercase:
      alphabet = string.ascii_lowercase

    # No numbers allowed!
    else:
      print "You entered a letter not in the alphabet. We'll skip this!"
      continue

    # Determine the position of this letter in the selected alphabet.
    index_in_alphabet = alphabet.index(letter)

    # We can just substract, because negative indices count from the end in
    # Python.
    new_s = new_s + alphabet[index_in_alphabet - 13]

  return new_s

print "Using '" + string.letters + "' as cipher alphabet."

# ROT13 is its own inverse!
print rot13(rot13("Rob"))
