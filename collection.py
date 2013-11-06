from twython import Twython
import json

class Twitter:

    FILE ='tweets.json'

    def authenticate(self, cred_fn=None):
        creds = self.load_creds(cred_fn)
        APP_KEY = creds['APP_KEY']
        APP_SECRET = creds['APP_SECRET']
        OAUTH_TOKEN = creds['OAUTH_TOKEN']
        OAUTH_TOKEN_SECRET = creds['OAUTH_TOKEN_SECRET']   
        self.twitter = Twython(APP_KEY, APP_SECRET,
                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


    def load_creds(self, cred_fn):
        infile = open(cred_fn)
        creds = json.load(infile)  
        return creds
    
    
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
        
        return jsono

tw = Twitter()   
jsono = tw.tweet_text()

text = (st['text'] for st in jsono['statuses'])
for t in text: print(t)
    