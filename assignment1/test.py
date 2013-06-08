import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
		tweet = json.loads(line)
		#print tweet.keys()
		#print "\n"
		if tweet.has_key("place"):
			if tweet["place"] != None:
				if tweet["place"]["country_code"] == "US":
					print tweet["place"]["full_name"][-2:]

if __name__ == '__main__':
    main()
