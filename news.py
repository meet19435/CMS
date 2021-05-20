import requests
from requests.auth import HTTPBasicAuth
import json

client_id = "Si1DR-_fdnT-7g"
secret_id = "mgP_3N40HkKFJsKH-NVNxdutq8Q0hQ"
user_agent = "cms2021"
redirect_url = "https://www.google.co.in/"

def authorization():                                                # returns a code which will be used for accessing the token, 
                                                                    # the code will be present on the redirected url
    url = "https://www.reddit.com/api/v1/authorize"
    data = {"client_id":client_id, 
            "response_type":"code","state":"ae562",
            "redirect_uri":redirect_url,"scope": "read",
            "duration":"permanent"}
    
    response = requests.get(url, params = data)
#     print(response.url)


def access_token_for_first_time(code):                              # for retrieving the access token  
    url = "https://www.reddit.com/api/v1/access_token"
    data={"grant_type":"authorization_code",
          "code": code,
          "redirect_uri":redirect_url}
    
    response = requests.post(url, data = data,
                            auth=(client_id,secret_id),
                            headers={"User-Agent":"cms2021"})
    response_data = response.json()                                 # dictionary containing access token and referesh token
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    return access_token,refresh_token


def access_refresh_token(refresh_token):                            # for refershing the access token
    url = "https://www.reddit.com/api/v1/access_token"
    data={"grant_type":"refresh_token","refresh_token":refresh_token}
    
    response = requests.post(url, data = data,
                            auth=(client_id,secret_id),
                            headers={"User-Agent":"cms2021"})
    response_data = response.json()
    access_token = response_data["access_token"]
    return access_token


def access_data_using_access_token(access_token):                   # for making api request to get news data
    
    response  = requests.get("https://oauth.reddit.com/r/IndiaNews/hot", 
                             headers = {"User-Agent":"cms2021","Authorization": "bearer "+access_token })
    news_data = response.json()
    return news_data

def get_news(data, news_display_count):                             # for selection of k news that will be displayed on website
                                                                    # news data is already fetched  
    news_arr = []
    secondary_news_arr = []
    news_without_images = []                                        # can be used as alternative
    
    for i in data["data"]["children"]:
        try:
            title  = i["data"]["title"]
            tag = i["data"]["link_flair_richtext"][0]["t"]
            link = i["data"]["url_overridden_by_dest"]
            try:
                image_link =i["data"]["thumbnail"]
                if(tag=="Crime &amp; Corruption" or tag=="Coronavirus"):    # our priority is to show news related crime and coronavirus
                    news_arr.append((title,tag,link,image_link))
                else:
                    secondary_news_arr.append((title,tag,link,image_link))
            except: 
                c=1
            news_without_images.append((title,tag,link,None))
        except:
            b = 1
            
    count = 0
    
    while(len(news_arr)<news_display_count and count< len(secondary_news_arr)):
        news_arr.append(secondary_news_arr[count])
        count +=1

    if(len(news_arr) == 0):
        # very less chances of this condition
        # Option 1 : Change subreddit
        # Option 2 : No news to display, currently using this
        C11=2
        return

    elif(len(news_arr)<news_display_count):
        count_1 = 0
        while(len(news_arr)<news_display_count):
            if(count_1>= len(news_arr)):
                count_1 = 0
            news_arr.append(news_arr[count_1])
            count_1 +=1
        
    return news_arr[:news_display_count]


def run(news_display_count):                                         # no of news to be displayed on website is taken as a input
    # code = authorization()                                         # neccessary to be called (once), we have already called it, thats why commented
    # code = "StGMrNVZPYDcz_O5_mJAeKBqVqwF_Q"                        # recieved code
    # access_token,refresh_token = access_token_for_first_time()     # neccessary to be called (once)
    refresh_token = "958457112293-OrYIQgBY_hFShbylSiEGI7IKeIPpAQ"    # refersh token is received when access token was retrieved for
                                                                     # first time (when access_token_for_first_time was called) 
    access_token = access_refresh_token(refresh_token)
    news_data = access_data_using_access_token(access_token)
    news_arr = get_news(news_data, news_display_count)
    return news_arr
    
