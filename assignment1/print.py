import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
result = json.load(response)
print result