print 'Hello World'

some_list = [12, 'monkeys']

some_string = 'julius'
some_string = some_string.upper()
some_string
# >>> 'JULIUS'

some_dict = {
  42: 'A completely irrelevant number'
}
some_dict[42]
# >>> 'A completely irrelevant number'

some_string[1]
# >>> 'U'

some_list[1]
# >>> 'monkey'

print 'Hello, World!'
print "Hello, World!"
print('Hello, World!')

# This function has no parameters and returns None.
def test_func_1():
  print "I'm useless!"

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

class MyTestClass:
  def __init__(self, name):
    self.name = name
  def say_hello(self, other_name):
    print self.name + ' says hi to ' + other_name
my_test_class_instance = MyTestClass('Rocko')
my_test_class_instance.say_hello('Clarissa')
# >>> 'Rocko says hi to Clarissa'

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

#favorite_color = \
  #raw_input('What is your favourite color? ')

def calculate_sp(player):
  bases = player['h'] + 2 * player['2b'] + \
    3 * player['3b'] + 4 * player['hr']
  return bases / float(player['ab'])

def calculate_obp(player):
  numerator = player['h'] + player['bb'] + player['hbp']
  denominator = player['ab'] + player['bb'] + \
    player['hbp'] + player['sf']
  return numerator / float(denominator)


player = {
  'name': 'Babe Ruth', 'ab': 458, 
  '1b': 73, '2b': 36, '3b': 9, 'hr': 54, 
  'h': 172, 'bb': 150, 'hbp': 3, 'sf': 0
} 

mays = {
  'name': 'Willie Mays', 'ab': 590,
  '1b': 85, '2b': 40, '3b': 15, 'hr': 50, 
  'h': 190, 'bb': 177, 'hbp': 5, 'sf': 1
}

teams = [
  'Montreal Expos', 'Washington Nationals',
  'San Francisco Giants', 'New York Yankees'
]

players = [
  player,
  mays
]

for player in players:
  sp = calculate_sp(player)
  obp = calculate_obp(player)
  print player['name']
  print 'OBP: ' + str(obp)
  print 'SP: ' + str(sp)
  print 'OPS: ' + str(obp + sp)

teams[0].upper() # 'MONTREAL EXPOS'

player['name'] # 'Babe Ruth'

teams.append('Krypton Krushers')

sum(player['h'], player['bb'])
