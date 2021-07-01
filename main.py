from apiclient.discovery import build
import time
import tweepy

#api key of twitter
consumer_key="*YOUR CONSUMER_KEY*"
consumer_secret='*YOUR CONSUMER_SECRET_KEY*'
access_token='*YOUR ACCESS_TOKEN*'
access_token_secret='*YOUR ACCESS_TOKEN_SECRET*'

#apikey of youtube
api_key="*YOUR API_KEY*"
youtube = build('youtube','v3',developerKey=api_key)
channel_id="*YOUR CHANNEL_ID*"  #you can find it from the https link of your channel

#for keeping track of last post
video_id=["None"]
playlist_id=["None"]


#twitter authentication
def OAuth():
  try:
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    print("Done")
    return auth
  except Exception as e:
    return None


#getting video ID to add to https link
def get_channel_videos(channel_id):

  msg=""

  ##if the upload id isnt there thus reducing the call of youtube API
  if(playlist_id[0]=="None"):
    playlist_id.pop(0)
    res=youtube.channels().list(id=channel_id,part='contentDetails').execute()
    playlist_id.append(res['items'][0]['contentDetails']['relatedPlaylists']['uploads'])



  latest_video=[]
  
  res = youtube.playlistItems().list(playlistId=playlist_id[0],part='snippet',maxResults=1).execute()

  latest_video.append(res)

  #checks the last video id which it tweeted matches or not

  if(video_id[0]!=latest_video[0]['items'][0]['snippet']['resourceId']['videoId']):

    video_id.pop(0)

    video_id.append(latest_video[0]['items'][0]['snippet']['resourceId']['videoId'])

    print(id,"\n")
    

  #for my tweet I have tagged bots that retweet your gaming tweet and thus increases your tweet reach you can add your tags here

    full_msg=["New video is up !\n","Title : ",latest_video[0]['items'][0]['snippet']['title'],"\nLink : https://www.youtube.com/watch?v=",latest_video[0]['items'][0]['snippet']['resourceId']['videoId'],"\nLike/Retweet","\nLink your YT/Twitch","\nFollow me","\n#smallstreamer","\n#SmallStreamersConnect","\n#SupportSmallStreams","\n#SupportSmallStreamers","\n@BlazedRTs","\n@sme_rt","\n@FmC_RTs","\n@PromoteAMGamers","\n@rtsmallstreams"]


  #this keeps the check for the word limit count of the tweet
    for str in full_msg:
      
      if((len(msg)+len(str))<=280):
        msg=msg+str
  
  else:
    msg= None

  print("\n",msg,"\n") 

  if(msg!=None):      
      oauth= OAuth()
      api=tweepy.API(oauth)
      api.update_status(msg)
      


if __name__ == "__main__":
  print("Bot started!")
  
  while(True):
    get_channel_videos(channel_id)
    time.sleep(3600)
    #I have kept the time to sleep as 3600 as it would reduce the chance of getting above the quota for calling youtube apis
