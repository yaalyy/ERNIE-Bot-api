import requests
import json
from config import api_key, secret_key

def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + api_key + "&client_secret=" + secret_key
        
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    
    response = requests.request("POST",url,headers=headers,data=payload)
    #return response
    return response.json().get("access_token")
    
def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "messages":[
            {
                "role": "user",
                "content": "你是一个AI小助手",
            }
        ]
    })
    
    response = requests.request("POST",url,headers=headers,data=payload)
    print(response.text)
    
if __name__ == '__main__':
    main()