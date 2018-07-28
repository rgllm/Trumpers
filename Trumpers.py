import tweepy

APP_KEY ='XxXxXxxXXXxxxxXXXxXX'
APP_SECRET ='XxXxXxxXXXxxxxXXXxXX'
OAUTH_TOKEN='XxXxXxxXXXxxxxXXXxXX'
OAUTH_TOKEN_SECRET='XxXxXxxXXXxxxxXXXxXX'
YOUR_ACCOUNT_NAME = 'XxXx'
TRUMP_USERID = '25073877' # @realDonaldTrump User ID. Do not change.

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Requires Authentication as of Twitter API v1.1
try:
    followers = api.friends_ids(screen_name = YOUR_ACCOUNT_NAME)
except error as e:
    print(e)

for follower_id in followers:
    print("Analyzing User: ",follower_id)
    if(api.show_friendship(source_id=follower_id,target_id=TRUMP_USERID)[0].following):
        try:
            print(str(follower_id) + " follows @realDonaldTrump")
            api.destroy_friendship(user_id=follower_id)
            unfollowedUser = api.get_user(follower_id)
            print(unfollowedUser.screen_name + " unfollowed!")
        except TwythonError as e:
            print(e)