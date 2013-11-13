from twython import TwythonStreamer
from util import credentials
import json

class MyStreamer(TwythonStreamer):
    #def on_success(self, data):
        #if 'text' in data:
            #print(data['text'])

    def on_success(self, data):
        count = 0
        filename = 'collection'
        output = open(filename + '.json', 'w')

        while count < 5000:
            if 'delete' in data:
                pass
            else:
                status = json.dumps(data, indent=4) + '\n'
                print(count)
                output.write(status)
                count += 1

        self.disconnect()
        output.close()

    #def collect(self, n=10, filename):
        #count = 0
        #if self.on_success(data):



    def on_error(self, status_code, data):
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()
    
    
users = [('ianbaxter_green','21085228'), ('brtgrn', '1625029752'),
         ('GreenYes2014', '1530835490'), ('InappreciableT','774219451')]

following = ', '.join([user[1] for user in users])

tags = 'greens, edinburgh, twitter'
    
stream = MyStreamer(*credentials('creds.json'))
#stream.statuses.filter(track=tags, follow=following)

stream.statuses.sample()


    