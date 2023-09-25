import requests
import json
from config import api_key, secret_key

def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?\
        grant_type=client_credentials&client_id=" + api_key + "&client_secret=" + secret_key