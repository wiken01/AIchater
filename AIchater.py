#AIchater.py
import itchat
import requests

def get_response(msg):
    api_url = "http://www.tuling123.com/openapi/api"
    data = {
            'key':'cfa3da11ea2245ff9775de478a2b84de',
            'info':msg,
            'userid':"wiken"
            }
    r = requests.post(api_url,data = data).json()
    return r.get("text")

@itchat.msg_register(itchat.content.TEXT,isGroupChat = True)
def print_content(msg):
    return get_response(msg['Text'])

itchat.auto_login()
itchat.run()