import requests
import json
from config import prompt
from chat_session import ChatSession
    
if __name__ == '__main__':
    
    if len(prompt) == 0:
        newSession = ChatSession()
    else:
        newSession = ChatSession(prompt=prompt)
    
    
    try:
        
        newResponse=newSession.start()
        print(">>"+ json.loads(newResponse.text)["result"])
        while True:
            print(">>",end="")
            newResponse = newSession.send(input())
            print(">>"+json.loads(newResponse.text)["result"])
    except TypeError:
        print("No response")
