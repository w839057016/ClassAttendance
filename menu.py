#encoding:utf-8
import os
import sys
import json
import wxconfig
import requests

def default_menu():
	menus = """
 {
     "button":[
     {
          "name":"考勤",
          "type":"click",
          "key":"verify"
      },{
          "name":"考勤结果推送",
          "type":"click",
          "key":"msg_send"
      }]
 }"""
	#data = json.dumps(buttons)
	url = wxconfig.WX_CREATE_MENU_API.format(wxconfig.get_token())
	r = requests.post(url,data=menus.encode('utf8'))
	print(r.text)
if __name__ == "__main__":
	default_menu()
