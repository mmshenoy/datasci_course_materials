import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    tags = {}
    top_ten = {}
		
    for line in tweet_file:
		tweet_json = json.loads(line)
		if tweet_json.has_key("entities"):
			entities = tweet_json["entities"]
			hashtags = entities["hashtags"]
			for i in range(0,len(hashtags)):
				hashtag = hashtags[i]
				tag = hashtag["text"]
				if tags.has_key(tag):
					tags[tag] += 1
				else:
					tags[tag] = 1
					
    max = []
    max.append("NA")
    max.append(-99999)
	
    if len(tags) >= 10:
		for i in range (0,10):
			for tag in tags:
				if tags[tag] > max[1]:
					max[0] = tag
					max[1] = tags[tag]
			
			top_ten[max[0]] = float(max[1])
			del tags[max[0]]
			max[0] = "NA"
			max[1] = -99999
	
    for tag in top_ten:
		print tag + " " + str(top_ten[tag])
		
if __name__ == '__main__':
    main()
