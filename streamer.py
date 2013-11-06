from twython import TwythonStreamer
from util import credentials

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, data):
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()
    
    
users = '@ianbaxter_green, @brtgrn, @GreenYes2014, @InappreciableT'
tags = 'green edinburgh'
    
stream = MyStreamer(*credentials('creds.json'))
stream.statuses.filter(track=tags, follow=users)