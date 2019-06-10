#encoding:utf-8
import  os
import  sys
import  time
import  threading
import  web
#等待20秒，期间处理人脸考勤，和消息推送
def thread_wait():
	print('\nthread started\n')
	for i in range(1,21):
		print(i)
		time.sleep(1)
	print('\nthread stoped\n')
	
#handle类，打开网址127.0.0.1:8080/wx直接调用GET方法
class handle:
	def GET(self):
		if True:
			#以下两行代码，启动一个线程
			t = threading.Thread(target=thread_wait)
			t.start()
			#线程没有执行完，可以直接return
			print('\nGet function\n')
			return 'OK'

#定义一个后缀
urls = (
	'/wx', 'handle',
)

#主函数
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()