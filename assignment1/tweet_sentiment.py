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
				print tweet
				words = tweet.split()
				count = 0
				for word in words:
					#print word
					if scores.has_key(word):
						#print word
						count += scores[word]
				print float(count)
			
if __name__ == '__main__':
    main()
