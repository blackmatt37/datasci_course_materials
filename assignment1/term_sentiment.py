import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
def calc(words, scores):
    total = 0
    for i in range(len(words)):
        if words[i].lower() in scores:
            total += scores[words[i].lower()]
    return total
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    unscored = {}
    for line in tweet_file:
        tweet = json.loads(str(line))
        if 'text' in tweet:
            text = tweet["text"].split(" ")
            number = calc(text,scores)
            for i in range(len(text)):
                if text[i].lower() not in scores:
                    if text[i].lower not in unscored:
                        unscored[text[i].lower()] = [float(number)]
                    else:
                        unscored[text[i].lower()].append(float(number))
    words = list(unscored.keys())
    #print unscored
    for i in range(len(words)):
        print words[i], sum(unscored[words[i]])/len(unscored[words[i]])
                
                    
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
