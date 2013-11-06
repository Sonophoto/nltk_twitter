import os
import json

from twython import Twython
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
        
        with open(fn) as infile:
            jsono = json.load(infile)
            
        text = (st['text'] for st in jsono['statuses'] if ['text'] in st)
        
        outfn = os.path.splitext(fn)[0] + '.txt'
        with open(outfn, 'w') as outfile:
            for t in text: 
                print(t, file=outfile)

tw = Twitter()   
jsono = tw.tweet_text()

    