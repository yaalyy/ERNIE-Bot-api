from config import Temperature,Top_p,Penalty_score,api_key,secret_key
import requests
import json



class ChatSession():
    def __init__(self,prompt=None) -> None:
        if prompt is None:
            if prompt is None:
                self.__prompt = "你好"
        else:
            self.__prompt = prompt
            
        self.__chat_history = []
        self.__access_token = ""
    
    def __get_access_token(self):
        url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + api_key + "&client_secret=" + secret_key
        
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
    
        response = requests.request("POST",url,headers=headers,data=payload)
        #return response
        self.__access_token = response.json().get("access_token")
        return self.__access_token

    def __insertSystemPrompt(self):
        self.__chat_history.append({"role": "user", "content": self.__prompt})
        
    def __generateResponse(self, temp_history):
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + self.__access_token
        headers = {
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "messages":temp_history,
            "temperature": Temperature,
            "top_p": Top_p,
            "penalty_score": Penalty_score,
        })
    
        response = requests.request("POST",url,headers=headers,data=payload)
        return response
    
    def start(self):     #only send the prompt and receive the response
        self.__get_access_token()
        self.__insertSystemPrompt()
        temp_history = self.__chat_history
        response = self.__generateResponse(temp_history=temp_history)
        temp_history.append({"role": "assistant", "content": json.loads(response.text)["result"]})
        self.__chat_history = temp_history
        return response
    
    def send(self,message):  #send the message from user and receive the response
        temp_history = self.__chat_history
        temp_history.append({"role":"user","content":message})
        response = self.__generateResponse(temp_history=temp_history)
        temp_history.append({"role": "assistant", "content": json.loads(response.text)["result"]})
        self.__chat_history = temp_history
        return response