import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    states = {}
    for line in sent_file:
		term, score = line.split("\t")
		scores[term] = int(score)
		#print scores.keys()
		
    for tweet in tweet_file:
		json_tweet = json.loads(tweet)
		#print json_tweet.keys()
		if json_tweet.has_key("text") and json_tweet.has_key("lang"):
			if json_tweet["lang"] == "en":
				tweet = json_tweet["text"].encode('utf-8')
				#print tweet
				words = tweet.split()
				count = 0
				for word in words:
					#print word
					if scores.has_key(word):
						#print word
						count += scores[word]
				#print float(count)
				if json_tweet.has_key("place"):
					if json_tweet["place"] != None:
						if json_tweet["place"]["country_code"] == "US":
							state = json_tweet["place"]["full_name"][-2:]
							if states.has_key(state):
								states[state] += count
							else:
								states[state] = count
								
    max = []
    max.append("NA")
    max.append(-999999)
	
    for state in states:
		#print state.encode("utf-8") + " " + str(states[state])
		if states[state] > max[1]:
			max[0] = state
			max[1] = states[state]
			
    print max[0]
	
if __name__ == '__main__':
    main()
