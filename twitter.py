from twython import Twython
import random
from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)
#Key values are generated from Twitter developer portal

twitter=Twython(
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)

messages = [ "messages go here" ] #this line is itentionally left blank.



#twitter.update_status(status=message) FOR TWEETING A MESSAGE
message = random.choice(messages)
twitter.update_status(status=message)
print("Tweeted: " + message)

#CRON JOB DETAILS
#sudo conrtab -e
#*/ * * * * python twitter.py 
#This will run this once every hour.
#python twitter.py
