# import relevant modules
import json
import urllib
import sys 

# define json clean-up function for making output prettier
def process_url(url):
    result = urllib.urlopen(url).read()
    loaded_result = json.loads(result)
    print json.dumps(loaded_result, sort_keys=True, indent=4)

# get user input - deprecated
# user_input = raw_input("Enter URL: ") - deprecated

# get user input from command line
user_input = sys.argv[1]

# run function
process_url(user_input)

# 
