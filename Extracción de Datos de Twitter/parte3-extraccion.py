import tweepy
import json

# 4 cadenas para la autenticacion
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

#Obtener informacion de un usario
data = api.me()
print json.dumps(data._json, indent=4)

#Obtener informacion de otros usarios
data = api.get_user("nike")
print json.dumps(data._json, indent=4)

#Obtener followers
data = api.followers(screen_name="nike")

for user in data:
    print json.dumps(user._json, indent=4)
print len(data)
 # Explicar cursor
for user in tweepy.Cursor(api.followers, screen_name="nike").items():
    print json.dumps(user._json, indent=4)

#Obtener followees
for user in tweepy.Cursor(api.friends, screen_name="nike").items(2):
    print json.dumps(user._json, indent=4)

#Obtener un timeline
for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike", tweet_mode="extended").items(10):
    print json.dumps(tweet._json,  indent=4)

#Buscar Tweets
for tweet in tweepy.Cursor(api.search, q="rusia 2018", tweet_mode="extended").items(5):
    print json.dumps(tweet._json, indent=4)

