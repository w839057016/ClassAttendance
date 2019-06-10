#encoding:utf-8
import os
import sys
import wxconfig
import requests

def save_img(path,img_name,media_id):
	try:
		url = wxconfig.WX_MEDIA_API.format(wxconfig.get_token(),media_id)
		print(url)
		r = requests.get(url)
		data = r.content
		with open(os.path.join(path,img_name),'wb') as f:
			f.write(data)
		print('file write successed ')
		return True
	except:
		return False
	