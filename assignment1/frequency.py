import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    terms = {}
    n = 0
		
    for line in tweet_file:
		tweet_json = json.loads(line)
		if tweet_json.has_key("text"):
			tweet = tweet_json["text"].encode("utf-8")
			words = tweet.split()
			
			for word in words:
				if terms.has_key(word):
					val = terms[word]
					val["count"] += 1
					terms[word] = val
				else:
					val = {}
					val["count"] = 1
					val["avg"] = 0
					terms[word] = val
	
    for key in terms:
		n += 1
	
    #print n
    if n > 0:
		for key in terms:
			val = terms[key]
			#print key + " " +str(val["count"])
			val["avg"] = val["count"]/float(n)
			print key + " " + str(val["avg"])
		
if __name__ == '__main__':
    main()
