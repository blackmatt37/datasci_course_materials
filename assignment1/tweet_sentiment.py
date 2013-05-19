import sys
import json
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    for line in tweet_file:
        tweet = json.loads(line)
        text = tweet["text"]
        words = text.split(" ")
        print words
        score = 0
        for word in words:
            score += scores[word.lower()]
        print float(score)
    hw()
    lines(afinnfile)
    lines(tweet_file)

if __name__ == '__main__':
    main()
