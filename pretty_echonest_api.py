# import relevant modules
import json
import urllib

# define json clean-up function for making output prettier
def process_url(x):
    result = urllib.urlopen(x).read()
    loaded_result = json.loads(result)
    print json.dumps(loaded_result, sort_keys=True, indent=4)

# get user input
user_input = raw_input("Enter URL: ")

# run function
process_url(user_input)

# 
