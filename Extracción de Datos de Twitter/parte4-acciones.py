import tweepy # >>> 3.8.0 <<<
import json

# 4 cadenas para la autenticacion
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


api.update_status("hmmmm")
ultimo_tweet_id = 'INSERTE AQUI ID DE UN TWEET'
api.retweet(ultimo_tweet_id)

# Dar like a un tweet
data = api.me()
id_ultimo_tweet = data._json["status"]["id"]
print id_ultimo_tweet

api.create_favorite(id_ultimo_tweet)
api.destroy_favorite(id_ultimo_tweet) # dislike

api.update_status("hmmmm x2", in_reply_to_status_id=id_ultimo_tweet) # responder a un tweet


# Subir una imagen
data_img = api.media_upload("./Picture1.jpg")
print data_img

# Subir la imagen en un tweet
api.update_status("hmmmmm", media_ids=["INSERTE AQUI ID DEL MEDIA SUBIDO"])

# Follow
api.create_friendship("nike")

# Unfollow
api.destroy_friendship("nike")

# Block
#api.create_block("nike")

# Unblock
#api.destroy_block("nike")

# Enviar DMs (requiere que tu app tenga acceso al Direct Message API)
id = api.me()._json["id"]
api.send_direct_message(id, text="hmmmmmmm")