# Allows us to convert the data Google returns from Javascript Object Notation
# (json) into a Python dictionary.
import json

# Provides function to ensure our term is sent in the right format. We can't
# have spaces in a URL, for example.
import urllib

# Handles the work of opening and reading from remote connections.
import urllib2

# The API URL that Google provides for command-line search services.
# By convention, constants in Python are written in uppercase.
API_URL = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='

##
# Return the estimated result count for the given search term.
def request_count(term):
  # Our request URL is the basic API URL, plus our search term. 
  # urllib.quote 'sanitizes' our term, to (among other things) replace spaces
  # with their URL-friendly '%20' equivalent.
  request_url = API_URL + urllib.quote(term)

  # Create a new request object for this URL.
  request = urllib2.Request(request_url)

  # Google requires that you tell them where you come from. This is the HTTP
  # header Referer, and it indicates to them who they can yell at if you abuse
  # their service (for a personal program, you might replace it with your 
  # email address... or gibberish).
  request.add_header('Referer', 'http://stanford.edu')
  
  # Get Google's response to our query. read() returns a string we can parse
  # with the json module.
  raw_response = urllib2.urlopen(request).read()

  # Load this response as a nested Python dictionary (a dictionary containing
  # other dictionaries as values), like {'a': {'b': {'c': 1}}}.
  # Try running some of these commands at the interpreter and inspecting the
  # results.
  response = json.loads(raw_response)

  # Main part of the response (there are other attributes as well, but we
  # want this.) json is a dictionary, as is json['responseData'] and
  # json['responseData']['cursor'].
  # So response looks something like:
  # {'responseData': 
  #   {'cursor':
  #      {'estimatedResultCount': 400000, other entries in cursor, ...},
  #     other entries in responseData,
  #     ...
  #   },
  #   other entries in the response dictionary,
  #   ...
  # }
  result_dict = response['responseData']['cursor']

  # The estimated result count is returned as a string, we coerce it into an
  # integer with int().
  return int(result_dict['estimatedResultCount'])



##
# Fight two terms against one another, and print the results.
def fight(term_a, term_b):
  term_a_count = request_count(term_a)
  term_b_count = request_count(term_b)
  
  # This is an example of string formatting, which allows you to enter
  # percent signs in a string and replace (interpolate) them with values.
  # Check out Python's documentation for more information and examples.
  winning_string = '%s wins over %s, %d to %d!'
  if term_a_count > term_b_count:
    print winning_string % (term_a, term_b, term_a_count, term_b_count)
  else:
    print winning_string % (term_b, term_a, term_b_count, term_a_count)
  
  return (term_a_count, term_b_count)
  
if __name__ == '__main__':
  fight('Stanford', 'UC Berkeley')

  print 'Now, try your own.'
  term_1 = raw_input('Enter a first fightin term: ')
  term_2 = raw_input('Enter a second fightin term: ')
  fight(term_1, term_2) 
  
