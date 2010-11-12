print 'Hello World'

some_list = [12, 'monkeys']

some_dict = {
  'New York': 'A state in the US.', 
  42: 'A completely irrelevant number.', 
  'today_is_sunday': False
} 

some_string = 'julius'
some_string = some_string.upper()
some_string
# >>> 'JULIUS'

some_dict[42]
# >>> 'A completely irrelevant number'

some_string[1]
# >>> 'U'

# This function has no parameters and...
def test_func_1():
  return 'returns a string.'

# This function has no parameters and returns None.
def test_func_2():
  pass

# This function has one parameter - a number.
# It adds 10 and returns that value.
# We could also write everything inline, like:
# 'return parameter_1 + 10'
def add_10(parameter_1):
  parameter_1 = parameter_1 + 10
  return parameter_1

green_eggs = 'green eggs and ham'
print green_eggs[6:10]

some_boolean = True
if some_boolean:
  print 'Truly today is a special day!'
else:
  print 'Back to the grind, peasant.'

strength = 15
if strength >= 15:
  print 'You pull the sword from the stone.'
  print 'All hail King Arthur!'
elif strength >= 10:
  print 'Solid effort.'
  print 'But you were born to work in the mines.'
else:
  print 'Nope! Not even close.'
  
customer_info = {
  'name': 'Rob Tirrell',
  'email': 'rpt@stanford.edu',
  'age': 24,
  'blood_sugar': 5.0, # mmol / L
  'likes_dark_chocolate': False,
  'astrological_sign': 'Gemini'
}

def compute_price(base_price, customer_info):
  pass # Fill in here!

if customer_info['age'] > 65:
  print 'Senior citizen discount!'

var = 44
var = 'The Life of Brian'
var = [
  'Episode IV: A New Hope', 
  'Episode V: The Empire Strikes Back', 
  'Episode VI: Return of the Jedi'
]
var = {
  'aardvark': 'a nocturnal burrower from Africa',
  'antbear': 'another name for an aardvark'
}

# Module that generates random numbers (among other things).
import random 
# Generate an integer from 1 to 6 (inclusive).
random.randint(1, 6)
# Generate an integer from 1 to *5* (inclusive).
random.randrange(1, 6)

lottery_players = [
  'Rufus',
  'Sun',
  'Tania',
  'Boris',
  'Rocky',
  'Daisy'
]

print random.choice(lottery_players)

random.shuffle(lottery_players)
number_of_players = len(lottery_players)
print 'Team 1:'
print lottery_players[:number_of_players / 2]
print 'Team 2:'
print lottery_players[number_of_players / 2:]

favorite_color = \
  raw_input('What is your favourite color? ')
