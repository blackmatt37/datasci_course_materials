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
    tweet_file = open(sys.argv[1])
    total = {}
    for line in tweet_file:
        tweet = json.loads(str(line))
        if 'text' in tweet:
            text = tweet["text"].split()
            for i in range(len(text)):
                if text[i].lower not in total and text[i].lower().split() != "":
                    total[text[i].lower()] = 1
                else:
                    total[text[i].lower()] += 1
    allTotal = 0.0
   # print total
    words = list(total.keys())
    for i in range(len(words)):
        allTotal += total[words[i]]
    for i in range(len(words)):
        thing = float(total[words[i]]/float(allTotal))
        print words[i].encode('utf-8'), thing
                
                    
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
