#encoding:utf-8
import os
import sys
import requests
import time
import json
cur_path = os.path.dirname(__file__)

#1.公众号的app和secret信息
WX_APPID = 'wxd04bb84eaa311017'
WX_SECRET = 'e323dc25add95c5cf472e1242a793619'

#2.获取token的连接
WX_TOKEN_API = "https://api.weixin.qq.com/cgi-bin/token?" + "grant_type=client_credential&appid={}&secret={}"
WX_MEDIA_API = "http://file.api.weixin.qq.com/cgi-bin/media/get?" + "access_token={}&media_id={}"
WX_CREATE_MENU_API = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={}"
WX_MSGTMP_API = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}"

#3.尝试使用文件保存的方式，将token进行保存
#3.1更新toke的方式
def get_token_by_api():
	#1.获取token
	url = WX_TOKEN_API.format(WX_APPID,WX_SECRET)
	r = requests.get(url)
	r_str = r.text
	r_dict = json.loads(r_str)
	expires_in = str(float(r_dict['expires_in'])+time.time())
	access_token = r_dict['access_token']
	#2.组成新的json
	file_dict = {'access_token':access_token,'expires_in':expires_in}
	file_str = json.dumps(file_dict)
	#3.写入文件信息
	with open(os.path.join(cur_path,'access_token.json'),'w') as f:
		f.write(file_str)
		print('new token write to file successed!')
	#写入文件
	return access_token
#3.2获取token的对外接口
def get_token():
	if not os.path.exists(os.path.join(cur_path,'access_token.json')):
		return get_token_by_api()
	with open(os.path.join(cur_path,'access_token.json'),'r') as f:
		s = f.read()
		s_dict = json.loads(s)
		expires_in = float(s_dict['expires_in'])
		access_token = s_dict['access_token']
		cur_time = time.time()
		print('\n'+str(cur_time) +'\n'+str(expires_in))
		#如果超时,更新
		if cur_time > expires_in:
			return get_token_by_api()
		else:
			return access_token
if __name__ == '__main__':
	print(get_token())
		