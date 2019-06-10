#encoding:utf-8
import os
import sys
import json
import requests
import wxconfig

def send_msg(toUser,msg_dict):
	student_id = msg_dict['student_id']
	course = msg_dict['course']
	day = msg_dict['day']
	time = msg_dict['time']
	grade = msg_dict['grade']
	room = msg_dict['room']
	teacher = msg_dict['teacher']
	params = ({
		"touser" : toUser,
		"template_id" : "AcXs-pWeKApUHzh4BWuntuMNsxodHV0cfrwqmBp1qNY",
		"url" : "http://exam.hhit.edu.cn/",
		"topcolor" : "#667F00",
		"data" : {
			"student_id" : {"value" :student_id , "color" : "#173177"},
			"course" : {"value" : course, "color" : "#173177"},
			"day" : {"value" : day, "color" : "#173177"},
			"time" : {"value" : time, "color" : "#173177"},
			"grade" : {"value" : grade, "color" : "#173177"},
			"room" : {"value" : room, "color" : "#173177"},
			"teacher" : {"value" : teacher, "color" : "#173177"}
		}
	})
	data = json.dumps(params)
	url = wxconfig.WX_MSGTMP_API.format(wxconfig.get_token())
	r = requests.post(url,data=data)
	print(r.text)