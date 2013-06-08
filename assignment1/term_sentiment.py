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
    terms = {}
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    for line in sent_file:
	    term, score = line.split("\t")
	    scores[term] = int(score)
		
    for line in tweet_file:
		tweet_json = json.loads(line)
		if tweet_json.has_key("lang") and tweet_json.has_key("text"):
			if tweet_json["lang"] == "en":
				tweet = tweet_json["text"].encode("utf-8")
				words = tweet.split()
				count = 0
				for word in words:
					if scores.has_key(word):
						count += scores[word]
				#print tweet
				#print count
				for word in words:
					if not scores.has_key(word):
						if terms.has_key(word):
							val_set = terms[word]
							if count >= 0:
								val_set["pcount"] += 1
								val_set["pscores"] += count
							else:
								val_set["ncount"] += 1
								val_set["nscores"] += count
							#val_set["average"] = val_set["average"]
							terms[word] = val_set
						else:
							val_set = {}
							if count >= 0:
								val_set["pcount"] = 1
								val_set["pscores"] = count
								val_set["ncount"] = 0
								val_set["nscores"] = 0
								val_set["pavg"] = 0
								val_set["navg"] = 0
							else:
								val_set["pcount"] = 0
								val_set["pscores"] = 0
								val_set["ncount"] = 1
								val_set["nscores"] = count
								val_set["pavg"] = 0
								val_set["navg"] = 0
							terms[word] = val_set
							
    for key in terms:
		val_set = terms[key]
		if val_set["pcount"] > 0:
			val_set["pavg"] = float(val_set["pscores"]/val_set["pcount"])
		if val_set["ncount"] > 0:
			val_set["navg"] = float(val_set["nscores"]/val_set["ncount"])
		print key + " " + str(val_set["pavg"]+val_set["navg"])

if __name__ == '__main__':
    main()
