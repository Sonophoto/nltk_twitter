import os
import json

from twython import Twython, TwythonStreamer
from util import credentials

class Twitter:

    FILE ='tweets.json'

    def authenticate(self, cred_fn):
        creds = credentials(cred_fn=cred_fn)
        self.twitter = Twython(*creds)

    def capture(self, fn=FILE, output=False):
        tweets = self.twitter.search(q='@OKFNAu')
        outfile = open(fn, 'w')       
        
        if output:
            print(json.dumps(tweets, sort_keys=True, indent=4, separators=(',', ': ')))
        else:
            json.dump(tweets, outfile)
                       
            
    def tweet_text(self, fn=FILE):
        
        infile = open(fn)
        jsono = json.load(infile)
        text = (st['text'] for st in jsono['statuses'] if ['text'] in st)
        
        outfn = os.path.splitext(fn)[0] + '.txt'
        outfile = open(outfn, 'w')
        for t in text: print(t, file=outfile)
        outfile.close()

tw = Twitter()   
jsono = tw.tweet_text()

    