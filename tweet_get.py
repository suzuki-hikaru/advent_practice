import tweepy
import config

CK=config.CK
CS=config.CS
AT=config.AT
AS=config.AS

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

woeid = {
    "日本": 23424856
}

for area, wid in woeid.items():
    print("--- {} ---".format(area))
    trends = api.trends_place(wid)[0]
    for i, content in enumerate(trends["trends"]):
        print(i+1, content['name'])