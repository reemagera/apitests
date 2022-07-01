import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()
API_KEY = os.getenv('API_KEY')
USER_ID = os.getenv('USER_ID')

response = requests.get("https://api.flickr.com/services//rest?",params={"method":"flickr.photos.getPopular","api_key":API_KEY,"format":"json","user_id":USER_ID})
assert(response.status_code == 200)
j = response.text[14:-1]
jsondata = json.loads(j)
length = len(jsondata["photos"]["photo"])
print("Select a number in between 1 to",length,": ")
idx = int(input())-1
photo = jsondata["photos"]["photo"][idx]
url = "https://live.staticflickr.com/"+photo["server"]+"/"+photo["id"]+"_"+photo["secret"]+".jpg"
print("Go to this url to view image:",url)