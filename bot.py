import requests
import twitter
import django
import urllib.request
import requests
from requests_oauthlib import OAuth1Session
import json
import time
from datetime import date

key=''
URL='https://api.fortnitetracker.com/v1/store'
CK=''
CS=''
AT=''
AS=''
twitter = OAuth1Session(CK,CS,AT,AS)

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"
   


def tweet(media_id,j,result):
    now_date = date.today()
    y = now_date.year
    m = now_date.month
    d = now_date.day
    len_pic = len(media_id)
    if len_pic == 4:
        tweet="{}年{}月{}日のショップその{}\n{} {}vBucks\n{} {}vBucks\n{} {}vBucks\n{} {}vBucks\n#Fortnite #フォートナイトショップ"
        status = tweet.format(y,m,d,j+1,result[j*4]['name'],result[j*4]['vBucks'],result[j*4+1]['name'],result[j*4+1]['vBucks'],
        result[j*4+2]['name'],result[j*4+2]['vBucks'],result[j*4+3]['name'],result[j*4+3]['vBucks'])
    elif len_pic == 3:
        tweet="{}年{}月{}日のショップその{}\n{} {}vBucks\n{} {}vBucks\n{} {}vBucks\n#Fortnite #フォートナイトショップ"
        status = tweet.format(y,m,d,j+1,result[j*4]['name'],result[j*4]['vBucks'],result[j*4+1]['name'],result[j*4+1]['vBucks'],
        result[j*4+2]['name'],result[j*4+2]['vBucks'])
    elif len_pic == 2:
        tweet="{}年{}月{}日のショップその{}\n{} {}vBucks\n{} {}vBucks\n#Fortnite #フォートナイトショップ"
        status = tweet.format(y,m,d,j+1,result[j*4]['name'],result[j*4]['vBucks'],result[j*4+1]['name'],result[j*4+1]['vBucks'])
    else:
        tweet="{}年{}月{}日のショップその{}\n{} {}vBucks\n#Fortnite #フォートナイトショップ"
        status = tweet.format(y,m,d,j+1,result[j*4]['name'],result[j*4]['vBucks'])
    media_id= ','.join(media_id)
    params = {"status": status, "media_ids": media_id}
    print(params)
    twitter.post(url_text,params=params)
    time.sleep(5)

def pic(media_id,i,j,result):
    img_url = result[i+4*j]['imageUrl']
    print(img_url)
    headers = {"User-Agent": "Mozilla/5.0"}
    request = urllib.request.Request(url=img_url,headers=headers)
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read()
    files = {"media" : data}
    req_media = twitter.post(url_media,files = files)
    media_id.append(json.loads(req_media.text)['media_id_string'])
    print(media_id)
    return media_id

def call():
    
    headers = {'TRN-Api-Key' : key}
    r = requests.get(URL, headers = headers)
    result = eval(r.text)
    print(len(result))
    print(result)
    num = len(result) // 4
    mod = len(result) % 4
    for j in range(0,num):
        media_id = []
        name = []
        vbucks = []
        for i in range(4):
            pic(media_id,i,j,result)
        tweet(media_id,j,result)
    media_id = []
    name = [shine tme]
    vbucks = [777777777777777777777777]
    for k in range(0,mod):
        pic(media_id,k,j+1,result)
    tweet(media_id,j+1,result)
    
        
if __name__ =='__main__':
    call()

            

