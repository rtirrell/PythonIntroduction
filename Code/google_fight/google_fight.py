# Allows us to convert the data Google returns into a Python dictionary.
import json

# Provides function to ensure our term is sent in the right format.
import urllib

# Handles the work of opening and reading from remote connections.
import urllib2

# This is the API URL that Google provides for command-line search services.
# By convention, constants in Python are written in uppercase.
API_URL = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='

def request_count(term):
  # Our request URL is the basic API URL, plus our search term. 
  request_url = api_url + urllib.quote(term)
  # Create a new request to this URL.
  request = urllib2.Request(request_url)
  # Google requires that you tell them where you come from.
  request.add_header('Referer', 'http://stanford.edu')
  
  # Get Google's response to our query.
  response = urllib2.urlopen(request).read()
  # Load this response as a nested Python dictionary (a dictionary containing
  # other dictionaries as values), like {'a': {'b': {'c': 1}}}.
  response_data = json.loads(response)

  # Main part of the response (there are other attributes as well, but we
  # want this.) json is a dictionary, as is json['responseData'] and
  # json['responseData']['cursor'].
  result_dict = response_data['responseData']['cursor']
  # The estimated result count is returned as a string, we coerce it into an
  # integer with int().
  count = int(result_dict['estimatedResultCount'])
  
  return count

def fight(term_a, term_b):
  term_a_count = request_count(term_a)
  term_b_count = request_count(term_b)
  
  winning_string = '%s wins over %s, %d to %d!'
  if term_a_count > term_b_count:
    print winning_string % (term_a, term_b, term_a_count, term_b_count)
  else:
    print winning_string % (term_b, term_a, term_b_count, term_a_count)
  
  return (term_a_count, term_b_count)
  
if __name__ == '__main__':
  fight('Stanford', 'UC Berkeley')
  
  # Hmmm, that was an easy win. Maybe they go by a different name?
  fight('Stanford', 'Cal')
  
  
