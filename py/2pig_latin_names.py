# Modify this to work with middle names too!
# Modify this to work with any sentence (ignoring periods).

def pig_latinize(s):
  s = s[1:] + s[0] + "ay"
  s = s.lower() 
  return s.capitalize()

name = raw_input("Please enter your first and last name: ")
first, last = name.split(" ")
print "Hello " + pig_latinize(first) + " " + pig_latinize(last) + "!"
